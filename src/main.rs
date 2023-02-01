use std::io;
use std::cmp::Ordering;
use rand::Rng;
// this works!
fn main() 
{
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

 /*
replace the expect call with a match expression that returns an Ok or Err 
value, and handles the expected error output rather than crashing
*/
    let guess: u32 = guess.trim().parse().expect("Please type a number!"); // add match here
    println!("You guessed: {guess}");

    println!("The secret number is: {secret_number}");
    
    loop {
        println!("Please input your guess.");
        let mut guess = String::new();
        
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

        let guess: u32 = guess.trim().parse().expect("Error-1!"); // add match here

        match guess.cmp(&secret_number) {
            Ordering::Less => {
                println!("Too small!");
                continue; // continue shouldn't be necessary here
            }
            Ordering::Greater => {
                println!("Too big!");
                continue; // continue shouldn't be necessary here
            }
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
