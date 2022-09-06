var strikes = 0
var balls = 0
var outs = 0

while true {
    print("type 's' for strike, 'b' for ball")
    print("input:")
    let input = readLine()

    if (input == "s") {
        strikes += 1
    }
    else {
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