
session="rdd"

tmux new-session -d -s $session

window=0
tmux rename-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=1
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=2
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=3
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=4
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=5
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=6
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=7
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=8
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

window=9
tmux new-window -t $session:$window -n "dzi$window"
tmux send-keys -t $session:$window "python run_sweep.py $window" C-m

tmux attach-session -t $session