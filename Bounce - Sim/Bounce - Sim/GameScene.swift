import SpriteKit
import GameplayKit

class GameScene: SKScene {
    
    let ball = SKShapeNode(circleOfRadius: 20)
    let wall = SKShapeNode(rectOf: CGSize(width: 20, height: 100))
    
    override func didMove(to view: SKView) {
        
        ball.fillColor = SKColor.blue
        ball.position = CGPoint(x: -100, y: 0)
        ball.physicsBody = SKPhysicsBody(circleOfRadius: 20)
        ball.physicsBody?.isDynamic = true
        ball.physicsBody?.affectedByGravity = false
        ball.physicsBody?.velocity = CGVector(dx: 200, dy: 0)  // Initial velocity
        ball.physicsBody?.linearDamping = 0
        ball.physicsBody?.restitution = 1  // Elastic collision
        
        wall.fillColor = SKColor.white
        wall.position = CGPoint(x: 200, y: 0)
        wall.physicsBody = SKPhysicsBody(rectangleOf: wall.frame.size)
        wall.physicsBody?.isDynamic = false  // Wall is static
    
        addChild(ball)
        addChild(wall)
    }
    
    override func update(_ currentTime: TimeInterval) {
        // Called before each frame is rendered
    }
}
