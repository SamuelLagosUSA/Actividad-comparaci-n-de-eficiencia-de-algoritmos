import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def factorial_recursivo(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def benchmark(func, n, veces=1):
    start = time.perf_counter()
    for _ in range(veces):
        resultado = func(n)
    end = time.perf_counter()
    tiempo_total = end - start
    tiempo_promedio = tiempo_total / veces
    mem = memory_usage((func, (n,)), max_iterations=1)
    memoria_max = max(mem) if mem else None
    return tiempo_promedio, memoria_max, resultado

if __name__ == "__main__":
    veces = 10000
    numeros = list(range(1, 21))
    tiempos_rec = []
    memorias_rec = []
    tiempos_it = []
    memorias_it = []

    for n in numeros:
        t_rec, m_rec, r_rec = benchmark(factorial_recursivo, n, veces)
        tiempos_rec.append(t_rec)
        memorias_rec.append(m_rec)
        t_it, m_it, r_it = benchmark(factorial_iterativo, n, veces)
        tiempos_it.append(t_it)
        memorias_it.append(m_it)
        print(f"[n={n}] Recursivo: {t_rec:.10f}s | {m_rec} MiB | resultado={r_rec}")
        print(f"[n={n}] Iterativo: {t_it:.10f}s | {m_it} MiB | resultado={r_it}")
        print("-" * 50)

    plt.figure(figsize=(10, 5))
    plt.plot(numeros, tiempos_rec, marker="o", label="Recursivo")
    plt.plot(numeros, tiempos_it, marker="o", label="Iterativo")
    plt.title("Tiempo promedio de ejecucion")
    plt.xlabel("n")
    plt.ylabel("Tiempo promedio (s)")
    plt.grid(True)
    plt.xticks(numeros)
    plt.legend()
    plt.savefig("comparacion_tiempo.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(numeros, memorias_rec, marker="o", label="Recursivo")
    plt.plot(numeros, memorias_it, marker="o", label="Iterativo")
    plt.title("Uso de memoria (pico por ejecucion)")
    plt.xlabel("n")
    plt.ylabel("Memoria (MiB)")
    plt.grid(True)
    plt.xticks(numeros)
    plt.legend()
    plt.savefig("comparacion_memoria.png")
    plt.close()

    print("Pruebas completadas. Graficas guardadas como 'comparacion_tiempo.png' y 'comparacion_memoria.png'")
