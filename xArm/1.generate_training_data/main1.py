from sg_range import SGRange
from moveonepoint import MoveOnePoint
from generateRRTpath import GenerateRRT

default_path = "/home/nishidalab07/github/Robot_path_planning_with_xArm/simulation1/"

sg_range = SGRange(default_path) 
moving = MoveOnePoint()
rrt_generator = GenerateRRT(default_path, time=3)

## 1-2 
# sg_range.sgrange()

## 1-3
# goal_positions = [  ]
# goal_positions = [-1.1590851893861092,-0.2729246527012283,-0.1090631356266123,-0.0038132811469293315,0.38246519188944855,0.39067986614253175]
# moving.movetopoint(goal_positions)

## 1-4
rrt_generator.move_to_sg(count=10000)
rrt_generator.save_times_csv()

# simulation1
# start_range
# min # goal_positions = [-0.1658429916135594,-0.1399699608363802,-0.5099227445917747,-0.0005763882525579187,0.37220893669441873,-0.26514396545471225]
# max # goal_positions = [0.437333859097476,-0.0399699608363802,-0.306977642700576,0.0017177637637269413,0.8513458438709504,0.43615549942072346]
# goal_range
# min # goal_positions = [-2.0000000000, -0.200000000, -0.6967717359, -0.003813281147, 0.3790173902, -0.4641266619]
# max # goal_positions = [-1.5500000000, -0.100000000, -0.3967717359, -0.001441490354, 1.137436831, 0.3906798661]

# simulation2
# start_range
# min # goal_positions = [-0.4215176695097176,  0.1000000000000, -0.9198909197019524, -0.0045485141109748, 0.70000000000000, -0.6280545377897786]
# max # goal_positions = [0.3812938592093262, 0.0000000000000, -0.399447544043225, 0.0123715644599728, 0.9908187325780036, 0.2210017193588722]
# goal_range
# min # goal_positions = [1.3500000000000, 0.000000000000, -2.402771587865023, 0.00000000000, 0.5250859823064351, -0.40000000]
# max # goal_positions = [1.463283131926562, 0.0292634896919041, -2.3597397337209944, 0.7692628705393734, 1.2527189482187342, 0.00000000000]