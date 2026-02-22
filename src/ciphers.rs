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

pub fn morse_code(text: &str, operation: &str) -> String {
    const MORSE_MAP: &[(char, &str)] = &[
        ('A', ".-"),
        ('B', "-..."),
        ('C', "-.-."),
        ('D', "-.."),
        ('E', "."),
        ('F', "..-."),
        ('G', "--."),
        ('H', "...."),
        ('I', ".."),
        ('J', ".---"),
        ('K', "-.-"),
        ('L', ".-.."),
        ('M', "--"),
        ('N', "-."),
        ('O', "---"),
        ('P', ".--."),
        ('Q', "--.-"),
        ('R', ".-."),
        ('S', "..."),
        ('T', "-"),
        ('U', "..-"),
        ('V', "...-"),
        ('W', ".--"),
        ('X', "-..-"),
        ('Y', "--.-"),
        ('Z', "--.."),
        ('0', "-----"),
        ('1', ".----"),
        ('2', "..--"),
        ('3', "...--"),
        ('4', "....-"),
        ('5', "....."),
        ('6', "-...."),
        ('7', "--..."),
        ('8', "---.."),
        ('9', "----."),
        ('.', ".-.-.-"),
        (',', "--..--"),
        ('?', "..--.."),
        ('!', "-.-.--"),
        ('/', "-..-."),
        ('(', "-.--."),
        (')', "-.--.-"),
        ('&', ".-..."),
        (':', "---..."),
        (';', "-.-.-."),
        ('=', "-...-"),
        ('+', ".-.-."),
        ('-', "-....-"),
        ('_', "..--.-"),
        ('$', "...-..-"),
        ('@', ".--.-."),
    ];

    if operation.to_lowercase() == "encrypt" {
        text.to_ascii_uppercase()
            .chars()
            .filter_map(|c| {
                // Look up the char in our array
                MORSE_MAP
                    .iter()
                    .find(|&&(ch, _)| ch == c)
                    .map(|&(_, code)| code)
            })
            .collect::<Vec<_>>()
            .join(" ") // Morse usually separates letters with a space
    } else {
        // Decryption logic: Split by space and look up the char
        text.split_whitespace()
            .filter_map(|code| {
                MORSE_MAP
                    .iter()
                    .find(|&&(_, m)| m == code)
                    .map(|&(ch, _)| ch)
            })
            .collect()
    }
}
