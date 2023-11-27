//
//  ContentView.swift
//  Todo
//
//  Created by Hargun Dadyala on 30/9/2023.
//

import SwiftUI

struct ContentView: View {
    @State private var Tasks: [String] = []
    @State private var New: String = ""
    
    var body: some View {
        VStack {
            List {
                ForEach(Tasks, id: \.self)
                {
                    task in Text(task)
                    
                } .onDelete(perform: delete)
            }
            
        }
        
        HStack{
            TextField("New Task", text:$New)
            Button("Add task") {
                if !New.isEmpty{
                    Tasks.append(New)
                    New = ""
                }
                    
            }
            
        }
        
    }
    
    func delete(at offsets: IndexSet) {
            Tasks.remove(atOffsets: offsets)
        }
    
}

#Preview {
    ContentView()
    }
