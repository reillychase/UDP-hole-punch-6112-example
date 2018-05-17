# UDP-hole-punch-6112-example
Allows players to join Battle.net games without port forwarding

For the last 20+ years, playing a battle.net or PvPGN game online has required port forwarding 6112 to your PC. Now there is a way around that.

If you are a PvPGN server admin, there is a way to allow all of your players to host without port forward, read on to find out how.

1. Publish JSON list of all player IP address
2. Take main.py and extend it to download that list of IPs, and send data to each of them periodically on port 6112 (as long as that is the port the game is configured to run on)
3. Now anyone can join your game
4. You would then compile main.py to an exe and ship it with the game client, run it when the game starts
