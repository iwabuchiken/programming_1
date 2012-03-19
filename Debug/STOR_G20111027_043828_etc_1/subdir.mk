################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../STOR_G20111027_043828_etc_1/lib.c \
../STOR_G20111027_043828_etc_1/main.c \
../STOR_G20111027_043828_etc_1/main3_get_max~v1u0.c 

OBJS += \
./STOR_G20111027_043828_etc_1/lib.o \
./STOR_G20111027_043828_etc_1/main.o \
./STOR_G20111027_043828_etc_1/main3_get_max~v1u0.o 

C_DEPS += \
./STOR_G20111027_043828_etc_1/lib.d \
./STOR_G20111027_043828_etc_1/main.d \
./STOR_G20111027_043828_etc_1/main3_get_max~v1u0.d 


# Each subdirectory must supply rules for building sources it contributes
STOR_G20111027_043828_etc_1/%.o: ../STOR_G20111027_043828_etc_1/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	gcc -DNULL=0 -I"C:\WORKS\PROGRAMS\MinGW\include" -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


