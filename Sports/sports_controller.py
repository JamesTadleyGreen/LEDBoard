#!/usr/bin/env python
import os
import datetime
import time
import subprocess
from queue import PriorityQueue
import argparse
import football_display as fd

def run_at(file, time):
    newruntime = time.strftime("%H:%M %d.%m.%Y")
    command = f'echo "python {file}" | at {newruntime} -m'
    print(command)
    return os.system(command)
# python ./sports_controller.py | at now -m

def list_python_processes():
    #ps = subprocess.Popen(('ps', '-ef'), stdout=subprocess.PIPE)
    output = str(subprocess.check_output(['ps', '-ef'])).split('\\n')
    output = [i for i in output if i.find('python') != -1]
    return output

def kill_all_python_processes():
    command = 'killall -9 python'
    return os.system(command)


#run_at('./football_display.py', datetime.datetime.now() + datetime.timedelta(minutes=1))
print(list_python_processes())
#kill_all_python_processes()

# create class
# runs at time and ouputs time of next match
# use this to create another class

class SportsScheduler():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--fixture_id", help="The ID of the next fixture", type=int)
        self.args = self.parser.parse_args()
        self.fixture_id = self.args.fixture_id

    def get_next_match(self):
        if not self.queue.empty():
            return self.queue.get()
        return None
    
    def run(self, next_fixture_id, next_game_time):
        run_at(f'./sports_controller.py --fixture_id={next_fixture_id}', next_game_time)


def run_game(fixture_id):
    if fixture_id == 592309:
        print('y')
        return 592308, datetime.datetime.now() + datetime.timedelta(minutes=1)
    else:
        print('n')
        return 592309, datetime.datetime.now() + datetime.timedelta(minutes=1)

# Main function
if __name__ == "__main__":
    # Splash screen for 5 mins before the game
    run_text = fd.RunText()
    # Run the game
    # Get the time of the next match and sleep until 5 minutes before
    ss = SportsScheduler()
    next_fixture_id, next_game_time = run_game(ss.fixture_id)
    ss.run(next_fixture_id, next_game_time)
    print('hi')
