
package CONVERSOR;

import java.util.Scanner;

public class ConversorBase {

// Método para convertir un número de cualquier base a decimal
    public static int convertirABaseDecimal(String numero, int baseOrigen) {
        return Integer.parseInt(numero, baseOrigen);
    }

    // Método para convertir un número decimal a cualquier base
    public static String convertirDeDecimalABase(int numeroDecimal, int baseDestino) {
        return Integer.toString(numeroDecimal, baseDestino).toUpperCase();
    }

    // Método para convertir un número de una base origen a una base destino
    public static String convertirNumero(String numero, int baseOrigen, int baseDestino) {
        // Convertir a decimal
        int numeroDecimal = convertirABaseDecimal(numero, baseOrigen);
        // Convertir de decimal a la base destino
        return convertirDeDecimalABase(numeroDecimal, baseDestino);
    }

    // Función para mostrar mensajes
    public static void message(String msg) {
        System.out.println(msg);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Menú principal
            message("--------CONVERSOR DE BASES-------");
            message("1. Convertir un Numero");
            message("2. Salir");
            message("Selecciona una opcion:");
            message("---------------------------------");

            int opcionSeleccionada = scanner.nextInt();
            scanner.nextLine();  // Consumir la nueva línea

            if (opcionSeleccionada == 2) {
                // Salir del programa
                message("Saliendo del programa.");
                break;
            }

            if (opcionSeleccionada != 1) {
                message("Opción no valida. Intente nuevamente.");
                continue;
            }

            // Solicitar al usuario el número a convertir
            message("Ingrese el numero a convertir:");
            String numero = scanner.nextLine();

            // Solicitar al usuario la base de origen
            message("Ingrese la base de origen (por ejemplo, 2 para binario, 8 para octal, 10 para decimal, 16 para hexadecimal):");
            int baseOrigen = scanner.nextInt();

            // Solicitar al usuario la base de destino
            message("Ingrese la base de destino (por ejemplo, 2 para binario, 8 para octal, 10 para decimal, 16 para hexadecimal):");
            int baseDestino = scanner.nextInt();

            // Validar las bases
            if (baseOrigen < 2 || baseOrigen > 36 || baseDestino < 2 || baseDestino > 36) {
                message("Base invalida. Las bases deben estar entre 2 y 36.");
                continue;
            }

            // Realizar la conversión
            String resultado = convertirNumero(numero, baseOrigen, baseDestino);

            // Mostrar el resultado
            message("--------------------------------------------------");
            message("El numero " + numero + " en base" + baseOrigen + ", es (" + resultado + ") en base " + baseDestino);
            message("--------------------------------------------------");
        }

        scanner.close(); // Cerrar el escáner
    }
}
