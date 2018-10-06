fn main() {
    let message = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"];
    let mut result = String::from("");
    for _char in message.iter() {
        result.push_str(_char)
    }
    println!("{}", result);
}