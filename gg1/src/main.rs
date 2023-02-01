use std::io;
use std::cmp::Ordering;
use rand::Rng;
// this works!
fn main() 
{
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);
// removed unneccessary code
    loop {
        println!("Please input your guess.");
        
        let mut guess = String::new();
        
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        }; // changed this expression to a match
       
        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win! The secret number is: {secret_number}");
                break;
            }
        }
    }
}
