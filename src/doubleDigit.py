import OpenGL.GL as gl
from settings import WIDTH, HEIGHT, A_RATIO

def addVertex(x:int, y:int):
  gl.glVertex3f(x/(WIDTH/2), y/(HEIGHT/2), 0)

def setRed():
  gl.glColor3f(0.95,0.2,0.2)
def setGreen():
  gl.glColor3f(0.2,0.95,0.2)
def setBlue():
  gl.glColor3f(0.2,0.2,0.95)

def resolveZone( x1: int, y1: int, x2: int, y2: int ):
  dx = x2-x1
  dy = y2-y1
  negativeDx, negativeDy, swap = False, False, False
  if dx < 0:
    dx=-dx
    negativeDx=True
  if dy < 0:
    dy=-dy
    negativeDy=True
  if dx < dy:
    dx, dy = dy, dx
    swap=True
  x1,y1 = zXto0(x1,y1,negativeDx, negativeDy, swap)
  x2,y2 = zXto0(x2,y2,negativeDx, negativeDy, swap)
  return x1,y1, x2,y2, dx, dy, negativeDx, negativeDy, swap

def z0toX(x: int, y: int, negativeDx:bool, negativeDy:bool, swap:bool):
  if swap:
    x,y=y,x
  if negativeDx:
    x=-x
  if negativeDy:
    y=-y
  return x,y

def zXto0(x: int, y: int, negativeDx:bool, negativeDy:bool, swap:bool):
  if negativeDx:
    x=-x
  if negativeDy:
    y=-y
  if swap:
    x,y=y,x
  return x,y

def mld8WayWithBegin( x1: int, y1: int, x2: int, y2: int):
  gl.glBegin(gl.GL_POINTS)
  mld8way( x1, y1, x2, y2)
  gl.glEnd()

def mld8way( x1: int, y1: int, x2: int, y2: int):
  x1, y1, x2, y2, dx, dy, negativeDx, negativeDy, swap = resolveZone(x1,y1,x2,y2)
  d = 2*dy - dx;
  dE = 2*dy;
  dNE = 2*(dy - dx);
  x,y=x1,y1
  while x!=x2 or y!=y2:
    displayX, displayY = z0toX(x, y, negativeDx, negativeDy, swap)
    # print(f"x,y: {x}, {y} ; displayX, displayY: {displayX}, {displayY}")
    addVertex(displayX, displayY)
    if (d>0):
      d = d + dNE
      y = y + 1
    else:
      d = d + dE;
    x = x + 1

_widthUnit = WIDTH//20
_heightUnit = HEIGHT//20
X0=-(_widthUnit*7)
X1=-(_widthUnit*2)
Y0=-_heightUnit*7
Y1=0
Y2=_heightUnit*7

GAP = 5
DIGIT_DIST = _widthUnit*11

# horizontal
def h0(xt):
  mld8way(X0+GAP + xt , Y0-GAP, X1-GAP + xt , Y0-GAP)
def h1(xt):
  mld8way(X0+GAP + xt , Y1, X1-GAP + xt , Y1)
def h2(xt):
  mld8way(X0+GAP + xt , Y2+GAP, X1-GAP + xt , Y2+GAP)

# vertical
def vr1(xt):
  mld8way(X1+GAP + xt , Y1+GAP, X1+GAP + xt , Y2-GAP)
def vl1(xt):
  mld8way(X0-GAP + xt , Y1+GAP, X0-GAP + xt , Y2-GAP)
def vr0(xt):
  mld8way(X1+GAP + xt , Y0+GAP, X1+GAP + xt , Y1-GAP)
def vl0(xt):
  mld8way(X0-GAP + xt , Y0+GAP, X0-GAP + xt , Y1-GAP)

def drawDigit(d:int, xt=0):
  if d>9:
    print("digit above 9 so it wont work")
    d=9
  if d not in [5,6]: # upper right vertical
    vr1(xt);
  if d != 2: # lower right vertical
    vr0(xt);
  if d in [0,4,5,6,8,9]: # vertical left upper
    vl1(xt);
  if d in [0,2,6,8]: # vertical left upper
    vl0(xt);
  if d in [0,2,3,5,6,8,9]: # horizontal ground
    h0(xt);
  if d not in [1,4]: # horizontal roof
    h2(xt);
  if d in [2,3,4,5,6,8,9]: # horizontal middle line
    h1(xt);

def drawNumber(i=20101491):
  d0 = (i//10) % 10
  d1 = i%10
  drawDigit(d0)
  drawDigit(d1, DIGIT_DIST)