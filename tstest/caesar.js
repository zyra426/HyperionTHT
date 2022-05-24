// Function: Caesar Cipher
const caesar_cipher = (T, shift) => {
    // Alphabet
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    // Encoded Text
    let encodedText = '';
    if (shift > 26) {
        shift = shift % 26;
    }
    let i = 0;
    while (i < T.length) {
        // Valid Alphabet Characters
        if (alphabet.indexOf(T[i]) !== -1) {
            // Find Alphabet Index
            const alphabetIndex = alphabet.indexOf((T[i]).toUpperCase());
            // Alphabet Index Is In Alphabet Range
            if (alphabet[alphabetIndex + shift]) {
                // Append To String
                encodedText += alphabet[alphabetIndex + shift];
            }
            // Alphabet Index Out Of Range (Adjust Alphabet By 26 Characters)
            else {
                // Append To String
                encodedText += alphabet[alphabetIndex + shift - 26];
            }
        }
        // Special Characters
        else {
            // Append To String
            encodedText += T[i];
        }
        // Increase I
        i++;
    }
    return encodedText;
};
//printing the output to terminal to test for correct output
//should print THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.
console.log(caesar_cipher('GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.', 39))