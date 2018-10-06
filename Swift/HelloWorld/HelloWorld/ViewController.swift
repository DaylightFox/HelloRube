//
//  ViewController.swift
//  HelloWorld
//
//  Created by Ardlan Khalili on 10/5/18.
//  Copyright © 2018 Ardlan Khalili. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    let HelloWorld: UILabel = {
        let label = UILabel()
        label.text = "Hello World!!"
        label.textColor = .black
        label.font = UIFont.boldSystemFont(ofSize: 50.0)
        label.textAlignment = .center
        label.translatesAutoresizingMaskIntoConstraints = false
        return label
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        view.addSubview(HelloWorld)
        HelloWorld.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
        HelloWorld.leftAnchor.constraint(equalTo: view.leftAnchor, constant: 20).isActive = true
        HelloWorld.rightAnchor.constraint(equalTo: view.rightAnchor, constant: -20).isActive  = true
        HelloWorld.heightAnchor.constraint(equalToConstant: 400).isActive = true
    }


}

