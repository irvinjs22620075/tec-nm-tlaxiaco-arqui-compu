# Lenguaje ensamblador

## Introduccion

El lenguaje ensamblador es un lenguaje de programación de bajo nivel que permite a los programadores escribir instrucciones que son ejecutadas directamente por la CPU. A diferencia de los lenguajes de alto nivel, como C o Java, el lenguaje ensamblador es específico de la arquitectura de la CPU y requiere un conocimiento detallado de la misma para poder programar en él.

El lenguaje ensamblador se caracteriza por su cercanía al hardware y su capacidad para manipular directamente los registros y la memoria de la CPU. Esto lo hace ideal para programar aplicaciones que requieren un alto rendimiento y un control preciso sobre el hardware, como los sistemas operativos, los controladores de dispositivos y los programas de tiempo real.

En esta guía, veremos los conceptos básicos del lenguaje ensamblador y cómo se utilizan para programar aplicaciones en sistemas basados en la arquitectura x86_x64.

```mermaid
graph LR
    A[Programa en C] --> B[Compilador]
    B --> C[Código ensamblador]
    C --> D[Ensamblador]
    D --> E[Programa en lenguaje máquina]
```

## Ciclo de vida de un programa compilado

El ciclo de vida de un programa compilado consta de varias etapas, que van desde la escritura del código fuente hasta la ejecución del programa en la CPU. Estas etapas son las siguientes:

1. **Código fuente:** Se definen las instrucciones y los datos que forman el programa en un lenguaje de alto nivel, como C o Java.

```c
#include <stdio.h>

int main() {
    printf("Hola, mundo!\n");
    return 0;
}
```

2. **Compilación:** El código fuente se traduce a código ensamblador por el compilador.

```assembly
section .data
    msg db 'Hola, mundo!', 0

section .text
    global _start

_start:
    mov eax, 4
    mov ebx, 1
    mov ecx, msg
    mov edx, 13
    int 0x80

    mov eax, 1
    mov ebx, 0
    int 0x80
```

3. **Ensamblado:** El código ensamblador se traduce a lenguaje máquina por el ensamblador.

```assembly
00000000  B804000000        mov eax,0x4
00000005  BB01000000        mov ebx,0x1
0000000A  B9E8040000        mov ecx,0xe8
0000000F  BA0D000000        mov edx,0xd
00000014  CD80              int 0x80
00000016  B801000000        mov eax,0x1
0000001B  BB00000000        mov ebx,0x0
00000020  CD80              int 0x80
```

4. **Programa en lenguaje máquina:** El programa en lenguaje máquina se ejecuta en la CPU.

### Etapas del compilado

1. **Preprocesamiento:** Se eliminan los comentarios, se expanden las macros y se incluyen los archivos de cabecera.

```bash
gcc -E programa.c -o programa.i
```

2. **Ensamblado:** Se traduce el código fuente a código ensamblador.

```bash
gcc -S programa.i -o programa.s
```

3. **Compilación:** Se crea el código objeto a partir del código ensamblador.

```bash
gcc -c programa.s -o programa.o
```

4. **Vinculación:** Se vinculan los archivos objeto para crear el programa ejecutable.

```bash
gcc programa.o -o programa
```

### Registros de la CPU

Los registros de la CPU son pequeñas áreas de almacenamiento que se utilizan para almacenar datos temporales y direcciones de memoria. Los registros son de tamaño fijo y se pueden acceder de forma muy rápida por la CPU. En la arquitectura x86_x64, los registros se dividen en varios tipos:

- **Registros de propósito general:** Se utilizan para almacenar datos temporales y direcciones de memoria. Los registros de propósito general son EAX, EBX, ECX, EDX, ESI, EDI, EBP y ESP.

- **Registros de segmento:** Se utilizan para almacenar los segmentos de memoria que se utilizan para acceder a la memoria. Los registros de segmento son CS, DS, ES, FS, GS y SS.

- **Registros de índice:** Se utilizan para almacenar los índices de los registros de segmento. Los registros de índice son SI, DI, BP y SP.

- **Registros de control:** Se utilizan para controlar el funcionamiento de la CPU. Los registros de control son CR0, CR2, CR3 y CR4.

- **Registros de depuración:** Se utilizan para depurar programas. Los registros de depuración son DR0, DR1, DR2, DR3, DR6 y DR7.

- **Registros de punto flotante:** Se utilizan para realizar operaciones aritméticas en punto flotante. Los registros de punto flotante son ST0, ST1, ST2, ST3, ST4, ST5, ST6 y ST7.

#### Registros de 64 bits

- **RAX:** Acumulador.
- **RBX:** Base.
- **RCX:** Contador.
- **RDX:** Datos.
- **RSI:** Índice fuente.
- **RDI:** Índice destino.
- **RBP:** Puntero base.
- **RSP:** Puntero pila.

#### Registros de 32 bits

- **EAX:** Acumulador.
- **EBX:** Base.
- **ECX:** Contador.
- **EDX:** Datos.
- **ESI:** Índice fuente.
- **EDI:** Índice destino.
- **EBP:** Puntero base.
- **ESP:** Puntero pila.

#### Registros de 16 bits

- **AX:** Acumulador.
- **BX:** Base.
- **CX:** Contador.
- **DX:** Datos.
- **SI:** Índice fuente.
- **DI:** Índice destino.
- **BP:** Puntero base.
- **SP:** Puntero pila.

#### Registros de 8 bits

- **AL:** Acumulador.
- **BL:** Base.
- **CL:** Contador.
- **DL:** Datos.
- **SIL:** Índice fuente.
- **DIL:** Índice destino.
- **BPL:** Puntero base.
- **SPL:** Puntero pila.

```plaintext
Registro de 64 bits
64                                  32                16       8
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
                                                               |--AL--|
                                                      |-------AX------|
                                    |----------------EAX--------------|
|----------------------------------RAX--------------------------------|
```

### Instrucciones de la CPU

Las instrucciones de la CPU son las operaciones que la CPU puede realizar en los datos almacenados en los registros y la memoria. Las instrucciones de la CPU se dividen en varios tipos:

- **Instrucciones de transferencia de datos:** Se utilizan para transferir datos entre los registros y la memoria. Las instrucciones de transferencia de datos son MOV, PUSH y POP.

- **Instrucciones aritméticas:** Se utilizan para realizar operaciones aritméticas en los datos almacenados en los registros. Las instrucciones aritméticas son ADD, SUB, MUL y DIV.

- **Instrucciones lógicas:** Se utilizan para realizar operaciones lógicas en los datos almacenados en los registros. Las instrucciones lógicas son AND, OR, XOR y NOT.

- **Instrucciones de salto:** Se utilizan para cambiar el flujo de ejecución del programa. Las instrucciones de salto son JMP, JZ, JNZ, JE, JNE, JA, JB, JAE, JBE, JL, JG, JLE y JGE.

- **Instrucciones de entrada y salida:** Se utilizan para leer y escribir datos desde y hacia los puertos de entrada y salida. Las instrucciones de entrada y salida son IN y OUT.

- **Instrucciones de manipulación de datos:** Se utilizan para manipular los datos almacenados en los registros. Las instrucciones de manipulación de datos son ROL, ROR, SHL, SHR, INC, DEC, NEG y NOT.

### Programación en ensamblador

La programación en ensamblador consiste en escribir instrucciones en lenguaje ensamblador que se traducen directamente a lenguaje máquina y se ejecutan en la CPU. La programación en ensamblador es útil para programar aplicaciones que requieren un alto rendimiento y un control preciso sobre el hardware, como los sistemas operativos, los controladores de dispositivos y los programas de tiempo real.

Para programar en ensamblador, es necesario tener un conocimiento detallado de la arquitectura de la CPU y de las instrucciones que puede ejecutar. También es necesario tener un conocimiento de los registros de la CPU y de cómo se utilizan para almacenar datos temporales y direcciones de memoria.

En esta guía, veremos cómo programar en ensamblador utilizando el lenguaje NASM en sistemas basados en la arquitectura x86_x64.

### Ejemplo de programa en ensamblador

A continuación se muestra un ejemplo de un programa en ensamblador que muestra un mensaje en pantalla:

```assembly
; section means that the following code is in the data section
; .data is the name of the section
section .data
    ; db (define byte) is used to define a string
    ; string is terminated by 0 (null character)
    ; msg is a label for the string "Hello, World!" 
    ; and will be used to refer to the string
    msg db "Hello, World!", 0

section .text
    ; global _start makes _start visible to the linker 
    ; so that it can be used as the entry point
    global _start

_start:
    ; mov is used to move data between registers
    ; eax is the accumulator register
    ; 4 is the system call number for sys_write
    mov eax, 4
    ; ebx is the first argument to the system call
    ; 1 is the file descriptor for stdout
    mov ebx, 1
    ; ecx is the second argument to the system call
    ; msg is the address of the string to print
    mov ecx, msg
    ; edx is the third argument to the system call
    ; 13 is the length of the string
    mov edx, 13
    ; int 0x80 is the assembly language instruction
    ; that generates a software interrupt (syscall)
    int 0x80

    ; exit
    mov eax, 1
    ; status code 0
    xor ebx, ebx
    ; int 0x80 is the assembly language instruction (syscall)
    int 0x80
```

## Referencias

[Guide to assembly language programming in linux](./resources/Springer%20-%20Guide%20to%20Assembly%20Language%20Programming%20in%20Linux.pdf)
