//
//  Requirements for building: https://gtk-rs.org/docs-src/requirements.html
//  Dependencies needed in Cargo.toml: gtk = "0.5.0"
//  Only tested on Manjaro Linux.
//

extern crate gtk;

use gtk::prelude::*;
use gtk::{Label, Window, WindowType};

fn main() {
    if gtk::init().is_err() {
        println!("GTK init failed.");
        return;
    }

    let hw_window = Window::new(WindowType::Toplevel);
    hw_window.set_title("HelloRube");
    hw_window.set_default_size(800, 400);

    let hw_label = Label::new(None);
    hw_label.set_markup("<span font='72'>Hello World!</span>");

    hw_window.add(&hw_label);
    hw_window.show_all();

    hw_window.connect_delete_event(|_, _| {
        gtk::main_quit();
        Inhibit(false)
    });

    gtk::main();
}
