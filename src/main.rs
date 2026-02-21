mod ciphers;

use axum::{Json, Router, routing::get, routing::post};
use clap::Parser;
use serde::Deserialize;
use serde_json::json;
use std::net::SocketAddr;
use tower_http::trace::TraceLayer;
use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    /// IP address to bind
    #[arg(long, default_value = "127.0.0.1")]
    host: String,

    /// Port to listen on
    #[arg(long, default_value_t = 3000)]
    port: u16,
}

#[derive(Deserialize)]
struct CipherRequest {
    text: String,
    operation: String,
    key: Option<i32>, // Use Option so ROT13 doesn't break
}

async fn caesar_handler(axum::Json(payload): Json<CipherRequest>) -> Json<serde_json::Value> {
    // Default the key to 0 if the user forgets to send it
    let key = payload.key.unwrap_or(0);

    let result = ciphers::caesar(&payload.text, key, &payload.operation);

    Json(json!({ "result": result }))
}

async fn rot13_handler(axum::Json(payload): Json<CipherRequest>) -> Json<serde_json::Value> {
    let result = ciphers::rot13(&payload.text, &payload.operation);

    Json(json!({
        "result": result
    }))
}

async fn home() -> Json<serde_json::Value> {
    Json(json!({
        "Use": {
            "URL": [
                { "/caesar": "encrypt or decrypt using Caesar Cipher" },
                { "/morsecode": "encrypt or decrypt using Morse Code" },
                { "/vignere": "encrypt or decrypt using Vignere Cipher" },
                { "/runningkeycipher": "encrypt or decrypt using Running Key Cipher" },
                { "/rot13": "encrypt or decrypt using ROT13 Algorithm" }
            ]
        },
        "Note": "MorseCode and ROT13 does not require a key to encrypt or decrypt"
    }))
}

#[tokio::main]
async fn main() {
    tracing_subscriber::registry()
        .with(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "example_crate=debug,tower_http=debug".into()),
        )
        .with(tracing_subscriber::fmt::layer())
        .init();

    let args = Args::parse();
    let addr: SocketAddr = format!("{}:{}", args.host, args.port)
        .parse()
        .expect("Invalid bind address");

    let app = Router::new()
        .route("/", get(home))
        .route("/caesar", post(caesar_handler))
        .route("/rot13", post(rot13_handler))
        .layer(TraceLayer::new_for_http());

    tracing::info!("Server running on {}", addr);

    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();

    axum::serve(
        listener,
        app.into_make_service_with_connect_info::<SocketAddr>(),
    )
    .await
    .unwrap();
}
