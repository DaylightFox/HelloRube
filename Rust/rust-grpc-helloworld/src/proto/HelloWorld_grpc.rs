// This file is generated. Do not edit
// @generated

// https://github.com/Manishearth/rust-clippy/issues/702
#![allow(unknown_lints)]
#![allow(clippy::all)]

#![cfg_attr(rustfmt, rustfmt_skip)]

#![allow(box_pointers)]
#![allow(dead_code)]
#![allow(missing_docs)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(trivial_casts)]
#![allow(unsafe_code)]
#![allow(unused_imports)]
#![allow(unused_results)]

const METHOD_HELLO_WORLD_SEND_HELLO: ::grpcio::Method<super::HelloWorld::Hello, super::HelloWorld::World> = ::grpcio::Method {
    ty: ::grpcio::MethodType::Unary,
    name: "/HelloWorld.HelloWorld/SendHello",
    req_mar: ::grpcio::Marshaller { ser: ::grpcio::pb_ser, de: ::grpcio::pb_de },
    resp_mar: ::grpcio::Marshaller { ser: ::grpcio::pb_ser, de: ::grpcio::pb_de },
};

#[derive(Clone)]
pub struct HelloWorldClient {
    client: ::grpcio::Client,
}

impl HelloWorldClient {
    pub fn new(channel: ::grpcio::Channel) -> Self {
        HelloWorldClient {
            client: ::grpcio::Client::new(channel),
        }
    }

    pub fn send_hello_opt(&self, req: &super::HelloWorld::Hello, opt: ::grpcio::CallOption) -> ::grpcio::Result<super::HelloWorld::World> {
        self.client.unary_call(&METHOD_HELLO_WORLD_SEND_HELLO, req, opt)
    }

    pub fn send_hello(&self, req: &super::HelloWorld::Hello) -> ::grpcio::Result<super::HelloWorld::World> {
        self.send_hello_opt(req, ::grpcio::CallOption::default())
    }

    pub fn send_hello_async_opt(&self, req: &super::HelloWorld::Hello, opt: ::grpcio::CallOption) -> ::grpcio::Result<::grpcio::ClientUnaryReceiver<super::HelloWorld::World>> {
        self.client.unary_call_async(&METHOD_HELLO_WORLD_SEND_HELLO, req, opt)
    }

    pub fn send_hello_async(&self, req: &super::HelloWorld::Hello) -> ::grpcio::Result<::grpcio::ClientUnaryReceiver<super::HelloWorld::World>> {
        self.send_hello_async_opt(req, ::grpcio::CallOption::default())
    }
    pub fn spawn<F>(&self, f: F) where F: ::futures::Future<Item = (), Error = ()> + Send + 'static {
        self.client.spawn(f)
    }
}

pub trait HelloWorld {
    fn send_hello(&mut self, ctx: ::grpcio::RpcContext, req: super::HelloWorld::Hello, sink: ::grpcio::UnarySink<super::HelloWorld::World>);
}

pub fn create_hello_world<S: HelloWorld + Send + Clone + 'static>(s: S) -> ::grpcio::Service {
    let mut builder = ::grpcio::ServiceBuilder::new();
    let mut instance = s.clone();
    builder = builder.add_unary_handler(&METHOD_HELLO_WORLD_SEND_HELLO, move |ctx, req, resp| {
        instance.send_hello(ctx, req, resp)
    });
    builder.build()
}
