### Pergunta
```
PP.1.2. Exemplifique a stemização e a lemazação de um texto, em língua espanhola. Ilustre 
um caso onde textos diferentes conduzem a uma mesma saída através do stemming ou 
lemmazaon. Considere como saída um vetor ordenado contendo lemas e stems.
PP.1.5. Repita PP.1.2. considerando a língua espanhola. 
```

### Resposta

***Stemização*** : Reduz cada palavra flexionadas ao seu stem. gerando assim uma outra palavra gramaticalmente incorreta, não necessariamente sendo idêntico à raiz morfológica da palavra.

```
Texto: Soy un texto que pide a gritos que lo procesen. Por eso yo canto, tú cantas, ella canta, nosotros cantamos, cantáis, cantan
['soy', 'un', 'text', 'que', 'pid', 'a', 'grit', 'que', 'lo', 'proces', '.', 'por', 'eso', 'yo', 'cant', ',', 'tu', 'cant', ',', 'ella', 'cant', ',', 'nosotr', 'cant', ',', 'cant', ',', 'cant']
```

***Lematização***: extrair a palavra base do termo, assim a classificação vocabular ou morfológica é considerada, e o resultado disso é sempre uma palavra que realmente existe na gramática. 

```
Texto: Soy un texto. Normalmente soy más largo y más grande. Que no te engañe mi tamaño.
['ser', 'uno', 'texto', '.', 'normalmente', 'ser', 'más', 'largo', 'y', 'más', 'grande', '.', 'que', 'no', 'tú', 'engañar', 'mi', 'tamaño', '.']
```