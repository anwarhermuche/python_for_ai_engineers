# Função que salva os logs de cada execução
def salvar_log(modelo: str,
               tokens_system_prompt: int,
               media_tokens_input: int,
               media_tokens_output: int,
               media_mensagens_por_dia: int,
               custo_total: float) -> None:
    with open("./modulo_3/log.txt", "a") as arquivo:
        arquivo.write(f"{modelo}, {tokens_system_prompt}, {media_tokens_input}, {media_tokens_output}, {media_mensagens_por_dia}, {custo_total}\n")

CUSTO_MODELOS_DOLAR = {
    "gpt-5.1": {"input": 1.25, "output": 10},
    "claude-4.5-opus": {"input": 5, "output": 25}
}

# Função que calcula o custo total
def calcular_custo_total(modelo: str,
                         tokens_system_prompt: int,
                         media_tokens_input: int,
                         media_tokens_output: int,
                         media_mensagens_por_dia: int) -> float:
    
    custo_input_modelo = CUSTO_MODELOS_DOLAR.get(modelo, {}).get("input", 0)
    custo_output_modelo = CUSTO_MODELOS_DOLAR.get(modelo, {}).get("output", 0)

    # k)
    # 1) system_prompt + input1
    # 1) output1
    # 2) system_prompt + input1 + output1 + input2
    # 2) output2
    # 3) system_prompt + input1 + output1 + input2 + output2 + input3
    # 3) output3
    # ...
    custo = 0
    for k in range(1, media_mensagens_por_dia + 1):
        custo_input = (tokens_system_prompt + k*media_tokens_input + (k-1)*media_tokens_output)*custo_input_modelo/1_000_000
        custo_output = media_tokens_output*custo_output_modelo/1_000_000
        custo_total = custo_input + custo_output

        custo = custo + custo_total
    
    custo_mensal = round(custo*30, 2)

    salvar_log(modelo, tokens_system_prompt, media_tokens_input,
               media_tokens_output, media_mensagens_por_dia, custo_mensal)
    
    return custo_mensal
    

