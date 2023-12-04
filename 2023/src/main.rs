mod day1;
mod day2;

use std::env;
use std::fs;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|_err| {
        println!("Usage: {} <day> <input_file>", &args[0]);
        process::exit(1);
    });

    match config.day.as_str() {
        "one" => day1::run(&config.input),
        "two" => day2::run(&config.input),
        _ => println!("Day not recognized"),
    }
}

struct Config {
    day: String,
    input: String,
}

impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("Not enough arguments");
        }

        let day = args[1].clone(); 
        let input_file = args[2].clone(); 

        let input = fs::read_to_string(input_file)
            .expect("Something went wrong reading the input file");

        Ok(Config { day, input })
    }
}
