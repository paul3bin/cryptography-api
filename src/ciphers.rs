pub fn rot13(text: &str, operation: &str) -> String {
    println!("Performing {}", operation);
    text.chars()
        .filter(|c| !c.is_whitespace())
        .map(|c| {
            let c = c.to_ascii_uppercase();
            if c.is_alphanumeric() {
                let base = b'A';
                (((c as u8 - base + 13) % 26) + base) as char
            } else {
                c
            }
        })
        .collect()
}

pub fn caesar(text: &str, key: i32, operation: &str) -> String {
    // If decrypting, just flip the key to negative
    let shift = match operation.to_lowercase().as_str() {
        "decrypt" => -key,
        _ => key, // Default to encrypt
    };

    text.chars()
        .filter(|c| c.is_ascii_alphabetic()) // Python's .isalpha()
        .map(|c| {
            let first_char = b'A' as i32;
            // Convert char to its ASCII number (like ord())
            let char_code = c.to_ascii_uppercase() as i8 as i32;

            // Apply shift with wrapping: (code - 'A' + shift) % 26 + 'A'
            let shifted = (char_code - first_char + shift).rem_euclid(26);

            (shifted + first_char) as u8 as char // Convert back (like chr())
        })
        .collect()
}
