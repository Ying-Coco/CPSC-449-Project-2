
ulimit -n 8192 &&
 xterm -e caddy &
xterm -e foreman start -m posts=3,accounts=3,msgs=3
