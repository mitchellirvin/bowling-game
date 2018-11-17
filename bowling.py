# CODE FILE

class Game():
    def __init__(self):
        self.currentScore = 0
        self.frames = [Frame() for i in range(10)]
        self.currentFrameIndex = 0
    
    def getScore(self):
        currentFrame = None
        for i in range(self.currentFrameIndex + 1):
            currentFrame = self.frames[i]
            self.currentScore += sum(currentFrame.pinsDowned)
            if currentFrame.state == 'SPARE':
                self.currentScore += self.frames[i + 1].pinsDowned[0]

        return self.currentScore 
    
    def addRoll(self, pinsDowned):
        currentFrame = self.frames[self.currentFrameIndex]
        currentFrame.addRoll(pinsDowned)
        if currentFrame.isFull:
            self.currentFrameIndex += 1


class Frame():
    def __init__(self):
        self.state = None
        self.pinsDowned = [0, 0, 0]
        self.rolls = 0
        self.isFull = False

    def addRoll(self, pinsDowned):
        self.pinsDowned[self.rolls] = pinsDowned
        if self.rolls == 1 and sum(self.pinsDowned) == 10:
            self.state = 'SPARE'
        self.rolls += 1
        if (self.rolls == 2):
            self.isFull = True

    



