import SwiftUI

var strikes = 0
var balls = 0
var outs = 0
var proc = 0

while true {
    print("type 's' for strike, 'b' for ball")
    print("input:")
    let input = readLine()
    if (input == "s") {
        proc == 0
    }
    else {
        proc == 1
    }

    if (proc == 0) {
        strikes += 1
    }
    else if (proc == 1) {
        balls += 1
    }
    print("Strikes: \(strikes)")
    print("Balls: \(balls)")
    print("Outs: \(outs)")    
    if (strikes >= 3) {
        outs += 1
        strikes -= strikes
    }
    if (outs >= 3) {
        break
    }
}