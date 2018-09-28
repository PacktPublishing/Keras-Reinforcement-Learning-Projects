import numpy as np

RMatrix = np.matrix([ [-1,50,1,-1,-1,-1],
		[-1,-1,-1,1,50,-1],
		[-1,-1,-1,1,-1,-1],
		[-1,-1,-1,-1,-1,100],
		[-1,-1,-1,50,-1,-1],
		[-1,-1,-1,-1,-1,100] ])

QMatrix = np.matrix(np.zeros([6,6]))


gamma = 0.9


InitialState = 0

def AllActions(state):
    CurrentState = RMatrix[state,]
    AllAct = np.where(CurrentState >= 0)[1]
    return AllAct

AvAct = AllActions(InitialState) 

def NextAction(AvActRange):
    NextAct = int(np.random.choice(AvAct,1))
    return NextAct

Action = NextAction(AvAct)

def Update(CurrentState, Action, gamma):
    
    MaxIndex = np.where(QMatrix[Action,] == np.max(QMatrix[Action,]))[1]

    if MaxIndex.shape[0] > 1:
        MaxIndex = int(np.random.choice(MaxIndex, size = 1))
    else:
        MaxIndex = int(MaxIndex)
    MaxValue = QMatrix[Action, MaxIndex]
    
    QMatrix[CurrentState, Action] = RMatrix[CurrentState, Action] + gamma * MaxValue

Update(InitialState,Action,gamma)

for i in range(10000):
    CurrentState = np.random.randint(0, int(QMatrix.shape[0]))
    AvAct = AllActions(CurrentState)
    Action = NextAction(AvAct)
    Update(CurrentState,Action,gamma)
    
print("Q matrix trained :")
print(QMatrix/np.max(QMatrix)*100)

CurrentState = 0
Steps = [CurrentState]

while CurrentState != 5:

    NextStepIndex = np.where(QMatrix[CurrentState,] == np.max(QMatrix[CurrentState,]))[1]
    
    if NextStepIndex.shape[0] > 1:
        NextStepIndex = int(np.random.choice(NextStepIndex, size = 1))
    else:
        NextStepIndex = int(NextStepIndex)
    
    Steps.append(NextStepIndex)
    CurrentState = NextStepIndex

print("Shortest path:")
print(Steps)
