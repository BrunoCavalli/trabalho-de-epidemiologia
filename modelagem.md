***

O crescimento de bactérias em ambientes aquáticos pode ser descrito por modelos matemáticos que relacionam a taxa de proliferação microbiana com variáveis ambientais, especialmente a temperatura. A literatura em microbiologia e biologia matemática indica que a temperatura é um dos principais fatores que determinam a taxa de crescimento bacteriano, influenciando diretamente a concentração de microrganismos em água doce e marinha.

Um dos modelos mais utilizados para descrever o crescimento populacional de microrganismos é o modelo exponencial, apresentado em diversas referências de biologia matemática, como em *Mathematical Biology*. Nesse modelo, o número de bactérias ao longo do tempo é dado por:

$$N(t) = N_0 e^{\mu t}$$

onde:
* $N(t)$ representa o número de bactérias no tempo $t$,
* $N_0$ é a quantidade inicial de bactérias,
* $\mu$ é a taxa específica de crescimento.

Entretanto, a taxa de crescimento bacteriano não é constante, sendo fortemente dependente da temperatura do meio. Estudos experimentais mostram que o aumento da temperatura, dentro de certos limites, acelera o metabolismo microbiano e aumenta a taxa de divisão celular. Para descrever essa dependência, um dos modelos mais utilizados é o proposto por David A. Ratkowsky:

$$\sqrt{\mu} = a(T - T_{\min})$$

onde:
* $\mu$ é a taxa de crescimento bacteriano,
* $T$ é a temperatura,
* $T_{\min}$ é a temperatura mínima para crescimento,
* $a$ é uma constante experimental.

Esse modelo, conhecido como modelo de Ratkowsky, é amplamente utilizado em microbiologia ambiental e em estudos preditivos de crescimento bacteriano, especialmente em faixas de temperatura subótimas para o microrganismo.

Substituindo a expressão da taxa de crescimento no modelo exponencial, obtém-se:

$$N(t) = N_0 e^{[a(T - T_{\min})]^2 t}$$

Essa equação mostra que a concentração de bactérias depende diretamente da temperatura, indicando que aumentos de temperatura podem resultar em crescimento exponencial da população bacteriana ao longo do tempo.

Além da modelagem determinística, a contagem de bactérias em amostras ambientais costuma ser tratada como uma variável aleatória discreta, pois o número de microrganismos em um volume de água resulta de eventos independentes e aleatórios. Por esse motivo, modelos probabilísticos são frequentemente utilizados para representar a distribuição do número de bactérias, sendo a distribuição de Poisson uma das mais empregadas em microbiologia e em análises de qualidade da água.

Nesse caso, o número de bactérias $X$ em uma amostra pode ser modelado por:

$$X \sim \text{Poisson}(\lambda)$$

onde $\lambda$ representa o número médio esperado de bactérias na amostra.

Considerando que essa média depende do crescimento bacteriano ao longo do tempo, define-se:

$$\lambda = N(t)$$

e, substituindo o modelo de crescimento dependente da temperatura, obtém-se:

$$\lambda = N_0 e^{[a(T - T_{\min})]^2 t}$$

Dessa forma, o modelo probabilístico completo indica que o número de bactérias segue uma distribuição de Poisson cuja média depende exponencialmente da temperatura. Esse resultado sugere que pequenas variações na temperatura da água podem produzir grandes variações na concentração bacteriana, especialmente em ambientes costeiros sujeitos a mudanças climáticas.

Em cenários de aquecimento global, nos quais a temperatura média da água aumenta ao longo do tempo, o modelo prevê elevação da taxa de crescimento microbiano e, consequentemente, da concentração esperada de bactérias. Esse comportamento é consistente com estudos que indicam que o aquecimento das águas superficiais pode favorecer a proliferação de microrganismos em ecossistemas marinhos e costeiros, afetando a qualidade da água e aumentando o risco de contaminação.

Assim, a combinação do modelo exponencial de crescimento, do modelo de dependência térmica de Ratkowsky e da distribuição de Poisson fornece uma estrutura matemática adequada para analisar o impacto do aumento da temperatura na concentração bacteriana em ambientes costeiros.

***