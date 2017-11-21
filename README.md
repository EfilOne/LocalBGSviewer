# LocalBGSviewer
A local BGS viewer / 3D starmap for Elite factions

## TODO
- Create IDLE script to query eliteBGS API at regular intervals
https://github.com/SayakMukhopadhyay/elitebgs/wiki
- Make map interactive with sidepanel showing more system infos on click
- Make graphs for system influence tracking (refreshes when clicking another system, should default on homesystem)
- Make the entire app usable with any faction, which implies :
	- UI to specify EDDB faction ID
	- EliteBGS limits to 10 systems, but make it able to grab more would be helpful
	- Above point creates a need for the map/grid to resize dynamically depending on furthest systems
