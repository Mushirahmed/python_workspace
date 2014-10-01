
from numpy  import *
from matplotlib import pyplot as plt
from scipy import signal
from control.timeresp import step_response
tau = 5.0*60
h_times = arange(0.0,10*tau,0.1)
sys = signal.lti(1,[1,1.0/tau])
step_response = sys.step(h_times)[1]
plt.plot(h_times,step_response/step_response.max())
plt.axhline(0.63, color='red')
plt.axvline(tau,color='red')
plt.xlabel('t')
plt.title('Step Response')
plt.show()
