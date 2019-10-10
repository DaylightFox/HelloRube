extern crate simple_logger;
extern crate futures;
extern crate grpcio;
#[macro_use]
extern crate log;

use std::thread;

mod server;
mod client;
mod proto;

fn main() {
    simple_logger::init();

    info!("Initializing server...");

    thread::spawn(move || server::start());

    info!("Starting client process...");

    client::start();
}
