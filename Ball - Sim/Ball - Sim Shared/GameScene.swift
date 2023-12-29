//
//  GameScene.swift
//  Ball - Sim Shared
//
//  Created by Hargun Dadyala on 11/10/2023.
//

import SpriteKit

class GameScene: SKScene, SKPhysicsContactDelegate {
    
    let ball = SKShapeNode(rectOf: CGSize(width: 20, height: 20))
    let bar = SKShapeNode(rectOf: CGSize(width: 20, height: 200))
    
    class func newGameScene() -> GameScene {
        // Load 'GameScene.sks' as an SKScene.
        guard let scene = SKScene(fileNamed: "GameScene") as? GameScene else {
            print("Failed to load GameScene.sks")
            abort()
        }
        
        // Set the scale mode to scale to fit the window
        scene.scaleMode = .aspectFill
        
        return scene
    }
    
    func setUpScene() {
        ball.fillColor = SKColor.white
        ball.physicsBody = SKPhysicsBody(circleOfRadius: 20)
        ball.physicsBody?.isDynamic = true
        ball.physicsBody?.affectedByGravity = false
        ball.physicsBody?.restitution = 1
        ball.physicsBody?.categoryBitMask = 1
        ball.physicsBody?.collisionBitMask = 2
        ball.physicsBody?.contactTestBitMask = 2
        ball.position = CGPoint(x: 0, y: 0)
        ball.physicsBody?.usesPreciseCollisionDetection = true
        addChild(ball)
        
        bar.fillColor = SKColor.white
        bar.physicsBody = SKPhysicsBody(rectangleOf: CGSize(width: 20, height: 200))
        bar.physicsBody?.isDynamic = false
        bar.physicsBody?.affectedByGravity = false
        bar.physicsBody?.categoryBitMask = 2
        bar.physicsBody?.collisionBitMask = 1
        bar.physicsBody?.contactTestBitMask = 1
        bar.position = CGPoint(x: -600, y: 0)
        addChild(bar)
        physicsWorld.contactDelegate = self
        
        self.physicsWorld.speed = 20
    }
    
    override func didMove(to view: SKView) {
        self.setUpScene()
        
        let moveLeft = SKAction.moveTo(x: -600, duration: 1)
        ball.run(moveLeft)
        
    }
    
    func didBegin(_ contact: SKPhysicsContact) {
        let collision = contact.bodyA.categoryBitMask | contact.bodyB.categoryBitMask

        // Ball-bar collision occurred

        if collision == 3 {
            // Ball hit bar
            if contact.bodyA.categoryBitMask == 1 {
                
                // Reverse the ball's velocity (change direction)
                ball.physicsBody?.velocity = CGVector(dx: -ball.physicsBody!.velocity.dx, dy: ball.physicsBody!.velocity.dy)
            }
            // Bar hit ball
            // Adjust the ball's velocity as needed
            else {
            }
        }
    }

    override func update(_ currentTime: TimeInterval) {
        // Called before each frame is rendered
        
        }
}

