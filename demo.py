
import PIDController


mein_regler = PIDController()

dein_regler = PIDController()



mein_regler.kp = 5.2

dein_regler.kp = 2.5

mein_regler.calculate_controller_output(100)




