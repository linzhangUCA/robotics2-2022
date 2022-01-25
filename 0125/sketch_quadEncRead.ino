const byte encA = 2;
const byte encB = 3;
int motorDir = 0;  // clockwise: 1, ccw: -1
long counts = 0;
int stateA = 0;
int stateB = 0;
int lastStateA = 0;
int lastStateB = 0;

void setup() {
  // setup pin modes
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(encA), ISR_updateA, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encB), ISR_updateB, CHANGE);
  stateA = digitalRead(encA);
  stateB = digitalRead(encB);
  lastStateA = stateA;
  lastStateB = stateB;
}

void ISR_updateA() {
  lastStateA = stateA;
  stateA = !stateA;
  if (lastStateA == 0) {
    if (lastStateB == 0) {
      motorDir = 1; // last states: {0,0}, present states: {1,0}
    }
    else {
      motorDir = -1;  // last states: {0,1}, present states: {1,1}
    }
  }
  else {
    if (lastStateB == 0) {
      motorDir = -1; // last states: {1,0}, present states: {0,0}
    }
    else {
      motorDir = 1;  // last states: {1,1}, present states: {0,1}
    }
  }
  counts += motorDir;
  motorDir = 0;
}

void ISR_updateB() {
  lastStateB = stateB;
  stateB = !stateB;
  if (lastStateA == 0) {
    if (lastStateB == 0) {
      motorDir = -1; // last states: {0,0}, present states: {0,1}
    }
    else {
      motorDir = 1;  // last states: {0,1}, present states: {0,0}
    }
  }
  else {
    if (lastStateB == 0) {
      motorDir = 1; // last states: {1,0}, present states: {0,1}
    }
    else {
      motorDir = -1;  // last states: {1,1}, present states: {1,0}
    }
  }
  counts += motorDir;
  motorDir = 0;
}


void loop() {

//  counts += motorDir;
  Serial.println(counts);
}
