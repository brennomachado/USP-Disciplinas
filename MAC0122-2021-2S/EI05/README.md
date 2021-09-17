EI05
Disponível a partir de: sexta, 20 ago 2021, 12:05
Data de entrega: quinta, 2 set 2021, 08:00
Arquivos requeridos: Fraction.py ( Baixar)
Tipo de trabalho: Trabalho individual

# Classe Fraction com frações irredutíveis
# Objetivos

O objetivo deste exercício é continuar a prática de programação conhecida como Orientação a Objetos e introduzir outros conceitos importantes para a análise de algoritmos. Mais especificamente vamos:

- discutir quando usar métodos e quando usar funções
- treinar a habilidade de reconhecimento de padrões
- medir tempo de execução

A classe Fraction usada nesse exercício é baseada na classe de mesmo nome da seção 1.13.1 Uma Classe Fraction do livro Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python.

# Estudos preliminares

- Mais sobre a implementação de operadores usando métodos especiais

# O que você deve fazer

Você pode usar o mesmo arquivo fraction.py que você entregou anteriormente e, caso desejar, pode também incluir as melhorias resultantes das discussões que você fez com seu time. Nesse exercício você deve copiar o método meu_mdc() em algum lugar apropriado em seu arquivo e alterar os demais métodos da sua classe para que represente/retorne frações irredutíveis. Por exemplo, a fração 10/15 não está em sua forma irredutível pois pode ser simplificada para sua forma irredutível 2/3.

Lembre-se que, para converter uma fração na sua forma irredutível, basta dividir o numerador e o denominador pelo mdc que, nesse exercício, deve ser calculado usando o método meu_mdc().
Método meu_mdc()

Modifique sua classe Fraction para que todas as frações criadas pela sua classe Fraction sejam irredutíveis usando o método meu_mdc() abaixo. Caso você já tenha tornado as frações irredutíveis usando alguma outra função ou método, modifique sua classe para que use apenas o seguinte método meu_mdc().

```
def meu_mdc( self, a, b ):
    ''' (Fraction, int, int) -> int 
    recebe dois inteiros a e b, e 
    retorna o mdc entre a e b.
    '''
    aa = abs(a)
    ab = abs(b)
    mdc = min(aa, ab)
    if mdc == 0: return max(aa, ab)
    while (aa % mdc != 0) or (ab % mdc != 0): 
        mdc -= 1
    return mdc
```

O método meu_mdc(a, b) calcula o máximo divisor comum entre os inteiros a e b de forma iterativa. Em particular, não utilize a função fornecida no livro pois vamos comparar o desempenho dessas funções mais tarde.
# o que mais você precisa fazer?

Além de usar o método meu_mdc() você deve completar a classe Fraction com os métodos

- \_\_gt__(self, other) (comparador “>” que compara se self é maior que other);
- \_\_le__(self, other) (comparador “<=” que compara se self é menor ou igual a other); e
- os métodos reversos correspondentes \_\_rgt__() e \_\_rle__().

Teste cada método antes de enviar sua solução e verifique que as frações usadas são irredutíveis. Lembre-se de testar com inteiros além de frações, segundo o cabeçalho de cada método.
Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- copie o seu arquivo fraction.py usado no exercício anterior. Caso não o tenha feito, faça o download do arquivo fraction.py desse exercício.
- carregue esse arquivo usando o Spyder ou Colab.
- caso não o tenha feito, leia o cabeçalho do arquivo fraction.py com atenção e edite o cabeçalho colocando seu nome e NUSP.
- execute o arquivo no Spyder ou no Colab. Observe que o arquivo original possui apenas algumas sugestões de teste. Você pode ter incluído outros testes durante os trabalhos em grupo. Complemente a função main() para testar os novos métodos.
- escreva os métodos novos e teste-os. Em caso de dúvidas, consulte novamente os exemplos do texto “Mais sobre a implementação de operadores usando métodos especiais”.
- após testar e corrigir os problemas que você identificou conferindo os resultados, teste de novo, até se certificar que todos os métodos se comportam corretamente.
- submeta apenas o arquivo fraction.py.

# Curiosidades

O módulo math do Python oferece a função gcd(), que tem o mesmo comportamento da nossa função meu_mdc(). Para a nossa próxima atividade, é importante que você use a função meu_mdc() em sua classe Fraction.
Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

# Arquivos requeridos
## Fraction.py