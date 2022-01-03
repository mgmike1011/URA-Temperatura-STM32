/*
 * PID_Controller.c
 *
 *  Created on: 3 sty 2022
 *      Author: mgmil
 */

#include "PID_Controller.h"
#include "main.h"

float u_pid_calculate(pid_controller_t* pid, float temp_zadana, float temp_aktualna){
	float u = 0, P, I, D, integral, derivative;
	pid->uchyb_aktualny = temp_zadana - temp_aktualna;
	//
	//Część proporcjonalna
	//
	P = pid->Kp*pid->uchyb_aktualny;
	//
	//Część całkująca
	//
	integral = pid->calka_poprzedni + pid->uchyb_aktualny + pid->uchyb_aktualny;
	pid->calka_poprzedni = integral;
	I = pid->Ki*integral*(pid->dt/2.0);
	//
	//Część różniczkująca
	//
	derivative = (pid->uchyb_aktualny - pid->uchyb_poprzedni)/pid->dt;
	pid->uchyb_poprzedni = pid->uchyb_aktualny;
	D = pid->Kd*derivative;
	//
	//Obliczenie sterowania
	//
	u = P + I + D;
	return u;
}

uint16_t saturation_pwm(float u){
	float counter_period = 999.0; //ZMIENIC!!!!!!
	float pwm_duty = (counter_period*u);
	uint16_t sat_pwm;
	if(pwm_duty < 0){
		sat_pwm = 0;
	}
	else if(pwm_duty > counter_period){
		sat_pwm = counter_period;
	}else{
		sat_pwm = pwm_duty;
	}
	return sat_pwm;
}
