/*
 * PID_Controller.h
 *
 *  Created on: 3 sty 2022
 *      Author: Agnieszka Piórkowska i Miłosz Gajewski
 */

#ifndef INC_PID_CONTROLLER_H_
#define INC_PID_CONTROLLER_H_
#include "stdio.h"
#include "stdint.h"

typedef struct{
	float Kp, Ki, Kd;
	float dt;
	float uchyb_poprzedni, calka_poprzedni, uchyb_aktualny;
}pid_controller_t;

float u_pid_calculate(pid_controller_t* pid, float temp_zadana, float temp_aktualna);
uint16_t saturation_pwm(float u);
#endif /* INC_PID_CONTROLLER_H_ */
