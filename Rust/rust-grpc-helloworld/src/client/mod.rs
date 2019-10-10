use super::proto::{HelloWorld as hello_world, HelloWorld_grpc as hello_world_grpc};

use std::io::{self, Read};
use std::sync::Arc;

use grpcio::{ChannelBuilder, EnvBuilder};
use hello_world_grpc::HelloWorldClient;
use hello_world::Hello;

pub fn start() {
    let env = Arc::new(EnvBuilder::new().build());
    let ch = ChannelBuilder::new(env).connect("127.0.0.1:50051");
    let client = HelloWorldClient::new(ch);

    info!("Client connected to 127.0.0.1:50051");

    let mut req = Hello::default();
    req.set_content("World".to_owned());
    let reply = client.send_hello(&req)
        .expect("Cannot send method");
    
    info!("From server recieved: {}...", reply.get_content());
}