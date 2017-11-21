from visual import *
from visual.graph import *
import wx
import os
import json
import request as r

version = '0.1a'
cor_ID = 26400

def translate(X,Y,Z):
	t_x = X + 114.78125
	t_y = Y - 80.71875
	t_z = Z + 4.875
	return (t_x,t_y,t_z)

# ---------- Request latest JSON digest from EliteBGS API ----------
folder = './data/'
if not os.path.exists(folder):
	os.makedirs(folder)
with open('./data/cor_systems.json','w') as f:
	f.write(r.cor_request())
with open('./data/losp_systems.json',"w") as f:
	f.write(r.losp_request())

# --------------------- Window management area ---------------------
w = window(menus=True,title='Local BGS Viewer '+version,x=0,y=0,width=800,
	height=800,style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)	# Create window

starmap = display(window=w,x=0,y=0,range=2,width=800,height=800)	# Define 3D display

for x,y in zip(range(-30,30,1), range(-30,30,1)):					# Generate grid
	if x % 10 or y % 10:
		g1_color = (0,0.2,0.2)
	else:
		g1_color = (0,0.4,0.4)
	curve(pos=[(x,0,-30), (x,0,30)],color=g1_color)
	curve(pos=[(-30,0,y),(30,0,y)],color=g1_color)

gdisplay(window=w)													# Invoke window

# --------------- Systems + Labels generation area ----------------
# Note : VPython uses a (x,z,y) coordinates system

cor_data = json.load(open('./data/cor_systems.json'))				# load CoR data from JSON
losp_data = json.load(open('./data/losp_systems.json'))				# load LOSP data from JSON

cor_systems = cor_data['docs']

# ------------------- Generate coordinates list -------------------
c = []
for coords in enumerate((sys['x'],sys['y'],sys['z']) for sys in cor_systems):
	c.append(coords[1])

cor_c = []
for sys_c in c:
	new_c = translate(sys_c[0],sys_c[1],sys_c[2])					# Run coordinates translation
	cor_c.append(new_c)

# --------------------- Generate label lists ----------------------
cor_sysn = []														# COR system names
for names in enumerate(sys['name'] for sys in cor_systems):
	cor_sysn.append(names[1])

cor_sysst = []														# COR system states
for states in enumerate(sys['state'] for sys in cor_systems):
	cor_sysst.append(states[1])

cor_sysinf =[]														# COR system influences
for factionlist in enumerate(sys['minor_faction_presences'] for sys in cor_systems):
	for f in factionlist[1]:
		if f['minor_faction_id'] == cor_ID:
			cor_sysinf.append(f['influence'])

# ----------------- Generate systems point cloud ------------------
points(pos=cor_c, size=10, color=color.red)							# Define points
for position, name, state, inf in zip(cor_c, cor_sysn, cor_sysst, cor_sysinf):
	label(pos=position, text=name.upper(),xoffset=25,yoffset=20,
		  height=12,font='sans',box=False, opacity=0.5)				# Generate name label
	label(pos=position, text=state,xoffset=25,yoffset=0,
		  height=12,font='sans',box=False, line=False, opacity=0.5)	# Generate state label
	label(pos=position, text=str(inf),xoffset=25,yoffset=-20,
		  height=12,font='sans',box=False, line=False, opacity=0.5)	# Generate influence label

# Keep display active for future development
while True:
    rate(1)
