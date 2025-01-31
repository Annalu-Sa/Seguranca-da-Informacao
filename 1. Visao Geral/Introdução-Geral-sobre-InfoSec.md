# Introdução Geral sobre InfoSec
Observação: este texto foi escrito para um trabalho universitário da disciplina Novas Mídias da UFRJ em 2024.2 por mim, então não espere um texto muito profundo ou específico sobre a área aqui.

## O que é Segurança da Informação (ou InfoSec)

Também conhecida como "*InfoSec*", a **Segurança da Informação** é um setor da área de  tecnologia da informação cuja finalidade é proteger dados, informações, sistemas, programas, equipamentos e redes de possíveis ameaças virtuais e/ou físicas. 

Desta forma, ela abrange um conjunto de atitudes, tecnologias e estratégias a serem seguidas para preservar o valor das informações, garantindo a sua *integridade*, *confidencialidade*, e *disponibilidade*. 

Algumas áreas de atuação da área:

* **Governança de Segurança da Informação**:

![governança de infosec](https://images.squarespace-cdn.com/content/v1/6048e1e3156d3f059791beae/1692983582379-AL6CU3H9AK9A7Z7856R5/governanca-da-seguranca-da-informacao-para-empresas-de-grande-porte-gateway-de-pagamento-iopay.png?format=1000w)

É uma área que trata de um conjunto de políticas, normas e métodos para guiar a forma que uma empresa deve ser conduzida, trata-se de uma vertente de segurança corporativa, que possui papel fundamental na mitigação de possíveis falhas na proteção de dados. 

Sob esse viés, a governança de segurança da informação garante:
1. o alinhamento dos objetivos de negócios na TI;
1. que os recursos de TI sejam usados de forma devida;
1. o estudo e preparo de implementações de novas tecnologias;
1. a revisão das medidas de segurança e a aplicação de softwares e hardwares;
1. treinamentos sobre as boas práticas de segurança aos/às colaboradores.
 
* **Cibersegurança**:

![Cibersegurança](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmWW9A4K_QEJkAfYJR7lI3BRShJbSnRB5jtw&s)

É uma área cujo objetivo é proteger sistemas, redes, programas, dados e equipamentos de ameaças cibernéticas a fim de evitar que operações comerciais sejam interrompidas, por exemplo.
    
Desta forma, as principais atividades de um/a profissional da área são:
1. Monitoramento de redes em busca de atividades suspeitas;
1. Investigar incidentes de segurança para identificar e mitigar eventos suspeitos;
1. Elaborar relatórios que detalham a atividade atual na rede e avaliam suas defesas;
1. Identificar pontos fracos da rede e conduzir testes contínuos para identificar vulnerabilidades.
      
* **Segurança de Aplicações**:

![Segurança de Aplicações](https://live.staticflickr.com/4477/23922032368_14f828ab0f_b.jpg)

Também conhecida como AppSec, é uma área que aborda um conjunto de práticas, processos e ferramentas que protegem aplicativos de ameaças cibernéticas para evitar o acesso não autorizado de criminosos a dados e informações confidenciais de uma organização.

Desta forma, algumas de suas funções são:
1. Identificar e corrigir vulnerabilidades no software;
1. Controlar o acesso a funções e informações;
1. Tornar inelegíveis os dados compartilhados por usuários através da encriptação.

## Importância
   Diante da Quarta Revolução Industrial, o cenário atual evidencia a intensa valorização dos dados no mercado, sejam eles de indivíduos ou de organizações, pois fornecem insights valiosos para planejamentos personalizados, inovação e eficiência operacional. Com o aumento do interesse nesses ativos, criminosos adaptam-se rapidamente e intensificam golpes virtuais com o intuito de roubá-los.
   Nesse contexto, tornou-se imprescindível a criação de uma área dedicada à proteção tanto de civis quanto de corporações contra ataques cibernéticos, chamada Segurança da Informação.
   Posto isso, vale explorar a importância e riscos atrelados aos dados individuais e organizacionais:
   
*Dados Individuais:*
- _Importância:_ dados pessoais permitem às empresas a criação de produtos e experiências customizadas, aumentando a satisfação do cliente e a competitividade. Ademais, com os dados é possível a criação de um perfil virtual do consumidor, possibilitando uma previsão de seu comportamento e aumentando o vínculo consumidor-empresa.

 - _Risco:_ quando vazados, tornam os usuários vulneráveis a roubo de identidade, fraudes financeiras, dentre outros. 

 - _Segurança:_ regulamentações como a LGPD (Lei Geral de Proteção de Dados) no Brasil exigem que as empresas protejam esses dados além de obter o consentimento dos usuários para coletá-los.
   
*Dados Organizacionais:*
 - _Importância:_ dados operacionais, financeiros e estratégicos melhoram a eficiência de processos e aumentam a resposta às demandas do mercado, possibilitando previsão de vendas por exemplo.
 - _Risco:_ roubo de segredos industriais, dados de clientes, documentos financeiros e outros que podem causar prejuízos econômicos e na reputação da empresa. 
 - _Segurança:_ instrução dos/as colaboradoras sobre ataques cibernéticos, desenvolvimento e fortalecimento de um plano de ação contra estes ataques, investir em Segurança da Informação.

## Pilares da Segurança da Informação
 A “Tríade CID” é um modelo que aborda os pilares da Segurança da Informação, sendo usada para identificar vulnerabilidades e criar soluções, além disso estas três letras significam Confidencialidade, Integridade e Disponibilidade.

A confidencialidade, integridade e disponibilidade são imprescindíveis para a operação de um negócio e o modelo CID segmenta essas ideias em pontos focais separados, a sua diferenciação é útil na orientação de equipes de segurança à medida que eles compreendem melhor suas especificidades e são capazes de identificar diversas formas pelas quais se pode abordar cada obstáculo.

![image](https://github.com/user-attachments/assets/691ce92e-5056-4839-b8b8-90ffaa811a9f)

Em detalhes, temos:


- **Integridade**: 
Ela garante que os dados, se autênticos, sejam confiáveis e livres de adulteração. Desta forma, se uma empresa fornece informações sobre colaboradores em seu site, essas informações precisam ter integridade. Além disso, uma pessoa com interesse em prejudicar a reputação da empresa pode tentar hackear seu site e alterar as descrições, ou quaisquer dados.
Comprometer a integridade geralmente é feito intencionalmente. Sob este viés um invasor é capaz de ignorar um sistema de detecção de intrusão (IDS), modificar configurações de arquivos ou alterar os registros mantidos pelo sistema para ocultar um ataque. Uma forma de verificar a integridade é o chamado ‘não repúdio’, que será tratado posteriormente.

- **Confidencialidade**: 
A confidencialidade abrange os esforços de uma corporação para garantir que os dados sejam mantidos em sigilo ou privados e, para isso, o alcance às informações deve ser controlado. Ademais, uma peça importante da manutenção da confidencialidade é assegurar que indivíduos sem autorização sejam impossibilitados de acessar ativos importantes para o negócio em questão.
Posto isto, para combater violações de confidencialidade, a empresa pode classificar e rotular dados restritos, habilitar políticas de controle de acesso, criptografar dados e usar sistemas de autenticação multifator (MFA). Vale mencionar também que é interessante garantir aos/às colaboradoras da organização o treinamento e o conhecimento necessários para reconhecer os perigos e evitá-los.

- **Disponibilidade**: 
A disponibilidade diz que os dados perdem seu valor quando não estão disponíveis para os colaboradores e/ou clientes usarem. Dessa forma, os sistemas, redes e aplicativos devem funcionar como previstos. Ademais, os indivíduos com acesso a informações específicas devem conseguir acessar estes dados quando for necessário e com um tempo aceitável a fim de não atrasar as operações da organização.
Assim, desastres naturais são um dos maiores obstáculos da disponibilidade, pois não é previsível e pode impedir que os usuários cheguem ao escritório e, por consequencia, interromper a disponibilidade de estações de trabalho e outros dispositivos que fornecem dados essenciais ao negócio. Um outro exemplo é a disponibilidade sendo comprometida por atos de sabotagem, como ataques de negação de serviço (DoS) ou ransomware.

Ademais, vale tratar de outros conceitos também importantes na área, como:

- **Autenticidade**: tem como objetivo determinar uma validade para a transmissão tanto da mensagem quanto do remetente para que o destinatário possa comprovar a origem e autoria de um dado documento.
- **Não-repúdio**: mencionado anteriormente na explicação da integridade, busca assegurar que o autor seja impossibilitado de negar a sua criação e assinatura em um documento.
- **Irretroatividade**: diz respeito a concepção de que novas políticas, leis ou mudanças de normas de segurança não devem ter implicações em eventos passados, ou seja, garante que o sistema não permita a confecção de documentos de forma retroativa no tempo.

## Principais Ameaças à Segurança da Informação

## Técnicas e Ferramentas de Proteção

## Educação, Consciencialização e Certificação

## Conclusão

## Referências
