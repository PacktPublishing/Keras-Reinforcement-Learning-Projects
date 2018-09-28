import gym
import numpy as np
env = gym.make('CartPole-v0')
HighReward = 0
BestWeights = None
for i in range(200):
  observation = env.reset()
  Weights = np.random.uniform(-1,1,4)
  SumReward = 0
  for j in range(1000):
    env.render()
    action = 0 if np.matmul(Weights,observation) < 0 else 1
    observation, reward, done, info = env.step(action)
    SumReward += reward
    print( i, j, Weights, observation, action, SumReward, BestWeights)
  if SumReward > HighReward:
    HighReward = SumReward
    BestWeights = Weights

observation = env.reset()
for j in range(1000):
  env.render()
  action = 0 if np.matmul(BestWeights,observation) < 0 else 1
  observation, reward, done, info = env.step(action)
  print( j, action)




