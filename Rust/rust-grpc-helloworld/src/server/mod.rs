use super::proto::{HelloWorld as hello_world, HelloWorld_grpc as hello_world_grpc};

use std::thread;
use std::io::{self, Read};
use std::sync::Arc;

use futures::sync::oneshot;
use futures::Future;

use grpcio::{ChannelBuilder, Environment, ResourceQuota, RpcContext, ServerBuilder, UnarySink};
use hello_world_grpc::{create_hello_world, HelloWorld};
use hello_world::{Hello, World};

#[derive(Debug, Clone)]
pub struct HelloWorldService;

impl HelloWorld for HelloWorldService {
    fn send_hello (&mut self, ctx: RpcContext<'_>, req: Hello, sink: UnarySink<World>) {
        let msg = format!("Hello, {}", req.get_content());
        let mut resp = World::default();
        resp.set_content(msg);

        let f = sink
            .success(resp)
            .map_err(move |e| error!("failed to send content, {:?}: {:?}", req, e));
        
        ctx.spawn(f);
    }
}

pub fn start () {
    let env = Arc::new(Environment::new(1));
    let service = create_hello_world(HelloWorldService);

    let mut server = ServerBuilder::new(env)
        .register_service(service)
        .bind("127.0.0.1", 50_051)
        .build()
        .unwrap();

    server.start();

    for &(ref host, port) in server.bind_addrs() {
        info!("listening on {}:{}", host, port);
    }

    let (tx, rx) = oneshot::channel();

    thread::spawn(move || {
        info!("Press ENTER to exit...");
        let _ = io::stdin().read(&mut [0]).unwrap();
        tx.send(())
    });

    let _ = rx.wait();
    let _ = server.shutdown().wait();
}
