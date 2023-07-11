class spaceObject
{
  constructor(x, y, size) {
      this.x = x;
      this.y = y;
      this.size = size;
  }
  getX(){
      return this.x;
  }
  getY(){
      return this.y;
  }
  getSize(){
      return this.size;
  }
  setX(x){
      this.x += x;
  }
  setY(y){
      this.y += y;
  }
  setSize(size){
      this.size += size;
  }
};