import streamlit as st

projetos = ["Estabelecer ciclo de otimização de produtividade através de tecnologias corporativas"]
mvps = ["Implantar procedimentos do Administrar e desenvolver pessoas no módulo RH do TOTVS"]
investimentos = ["120000,00"]
gestores = ["Tadeu"]
especialistas = ["Zé", "Jão"]
squads = ["Maria", "Joaquina", "Cirilo"]
equipe = [gestores, especialistas, squads]
entregas = ["Diagnóstico Detalhado dos Processos em nível de Automatização", "Identificar as tecnologias corporativas que melhor atendam às necessidades da organização", "Organizar, corrigir e implantar módulos de Backoffice da TOTVS", "Implementação do TOTVS Fluig e Método de Automatização de Processos com BPMS", "Desenvolvimento de Métodos de Otimização da Produtividade de Processos", "Estabelecer processos de Integração de Sistemas"]
resultados = ["Avanço na automatização de processos", "Avanço da Criação do repositório de documentos"]
metricas = ["% Avanço na automatização de processos", "% de Criação do repositório de documentos"]

def tableRow():

    projeto = projetos
    mvp = mvps
    investimento = investimentos

    htmlRow = f"""
        <div class="flex-row">
            <div class="box">
                <div class="box1">
                    <table class="table1">
                        <tr class="thead1">
                            <th>Projeto<img src="https://cdn-icons-png.flaticon.com/128/10484/10484735.png" alt="Icone da tabela Projetos" class="table-icon"></th>
                        </tr>
                        <tr class="tdata1">
                            <td>{projeto[0]}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="box">
                <div class="box2">
                    <table class="table2">
                        <tr class="thead2">
                            <th>MVP<img src="https://cdn-icons-png.flaticon.com/128/9238/9238294.png" alt="Icone da tabela MVPs" class="table-icon"></th>
                        </tr>
                        <tr class="tdata2">
                            <td>{mvp[0]}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="box">
                <div class="box3">
                    <table class="table3">
                        <tr class="thead3">
                            <th>Investimento<img src="https://cdn-icons-png.flaticon.com/128/7928/7928255.png" alt="Icone da tabela Investimentos" class="table-icon"></th>
                        </tr>
                        <tr class="tdata3">
                            <td>R${investimento[0]}</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    """
    return htmlRow

def tableEqp():
    gestor = gestores
    especialista = especialistas
    squad = squads

    htmlEqp = f"""
        <div class="box">
            <div class="box4">
                <table class="table4">
                    <tr class="thead4">
                        <th>Equipe<img src="https://cdn-icons-png.flaticon.com/128/5069/5069162.png" alt="Icone da tabela Equipe" class="table-icon"></th>
                    </tr>
                    <tr class="thead4-eqp">
                        <th><img src="https://cdn-icons-png.flaticon.com/128/3916/3916615.png" alt="Ícone do gestor para a tabela de Equipe" class="table-icon"> Gestor</th>
                    </tr>
                    <tr class="tdata4">
                        <td>{gestor[0]}</td>
                    </tr>
                    <tr class="thead4-eqp">
                        <th><img src="https://cdn-icons-png.flaticon.com/128/9795/9795619.png" alt="Ícone do especialista para a tabela de Equipe" class="table-icon"> Especialista</th>
                    </tr>
                    <tr class="tdata4">
                        <td>{especialista[0]}</td>
                    </tr>
                    <tr class="tdata4">
                        <td>{especialista[1]}</td>
                    </tr>
                    <tr class="thead4-eqp">
                        <th><img src="https://cdn-icons-png.flaticon.com/128/9856/9856655.png" alt="Ícone do squad para a tabela de Equipe" class="table-icon"> Squad</th>
                    </tr>
                    <tr class="tdata4">
                        <td>{squad[0]}</td>
                    </tr>
                    <tr class="tdata4">
                        <td>{squad[1]}</td>
                    </tr>
                    <tr class="tdata4">
                        <td>{squad[2]}</td>
                    </tr>
                </table>
            </div>
        </div>
    """
    return htmlEqp

def tableUnic():
    entrega = entregas

    htmlUnic = f"""
        <div class="box">
            <div class="box5">
                <table class="table5">
                    <tr class="thead5">
                        <th>Principais entregas<img src="https://cdn-icons-png.flaticon.com/128/10801/10801807.png" alt="Icone da tabela Principais entregas" class="table-icon"></th>
                    </tr>
                    <tr class="tdata5">
                        <td>{entrega[0]}</td>
                    </tr>
                    <tr class="tdata5">
                        <td>{entrega[1]}</td>
                    </tr>
                    <tr class="tdata5">
                        <td>{entrega[2]}</td>
                    </tr>
                    <tr class="tdata5">
                        <td>{entrega[3]}</td>
                    </tr>
                    <tr class="tdata5">
                        <td>{entrega[4]}</td>
                    </tr>
                    <tr class="tdata5">
                        <td>{entrega[5]}</td>
                    </tr>
                </table>
            </div>
        </div>
    """
    return htmlUnic

def tableCol():
    resultado = resultados
    metrica = metricas

    htmlCol = f"""
        <div class="flex-column">
            <div class="box">
                <div class="box6">
                    <table class="table6">
                        <tr class="thead6">
                            <th>Resultado esperado<img src="https://cdn-icons-png.flaticon.com/128/9797/9797853.png" alt="Icone da tabela Resultado esperado" class="table-icon"></th>
                        </tr>
                        <tr class="tdata6">
                            <td>{resultado[0]}</td>
                        </tr>
                        <tr class="tdata6">
                            <td>{resultado[1]}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="box">
                <div class="box7">
                    <table class="table7">
                        <tr class="thead7">
                            <th>Métricas<img src="https://cdn-icons-png.flaticon.com/128/7931/7931125.png" alt="Icone da tabela Métricas" class="table-icon"></th>
                        </tr>
                        <tr class="tdata7">
                            <td>{metrica[0]}</td>
                        </tr>
                        <tr class="tdata7">
                            <td>{metrica[1]}</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    """
    return htmlCol

def tableGeral():
    dadosRow = tableRow()
    dadosEqp = tableEqp()
    dadosUnic = tableUnic()
    dadosCol = tableCol()

    htmlGeral = f"""
        <div class="flex-container">
            <div>{dadosRow}</div>
            <div class="flex-row">
                <div>{dadosEqp}</div>
                <div>{dadosUnic}</div>
                <div>{dadosCol}</div>
            </div>
        </div>
    """
    return htmlGeral



canvaStyle = """body{
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #fff;
    }

    .box1,
    .box2,
    .box3,
    .box4,
    .box5,
    .box6,
    .box7{
        width: 100%;
        height: auto;
        max-width: 400px;
        margin: 5px;
        max-height: 400px;
        overflow: auto;
        overflow-x: hidden;
    }


    .box1:hover,
    .box2:hover,
    .box3:hover,
    .box4:hover,
    .box5:hover,
    .box6:hover,
    .box7:hover{
        transform: scale(0.98);
        border-radius: 20px;
    }

    .box1:hover{
        box-shadow: 0px 0px 25px rgba(74, 172, 252, 1);
    }

    .box2:hover{
        box-shadow: 0px 0px 25px rgba(255, 161, 189, 1);
    }

    .box3:hover{
        box-shadow: 0px 0px 25px rgba(255, 115, 84, 1);
    }

    .box4:hover{
        box-shadow: 0px 0px 25px rgba(73, 197, 57, 1);
    }

    .box5:hover{
        box-shadow: 0px 0px 25px rgba(141, 52, 135, 1);
    }

    .box6:hover{
        box-shadow: 0px 0px 25px rgba(255, 187, 78, 1);
    }

    .box7:hover{
        box-shadow: 0px 0px 25px rgba(255, 255, 68, 1);
    }

    .table1,
    .table2,
    .table3,
    .table4,
    .table5,
    .table6,
    .table7{
        width: 400px;
        border-collapse: collapse;
        border-radius: 10px;
        overflow: hidden; 
    }

    .thead1{
        background-color: #4aacfc;
    }

    .thead2{
        background-color: #ffa1bd;
    }

    .thead3{
        background-color: #ff7354;
    }

    .thead4{
        background-color: #49c539;
    }

    .thead5{
        background-color: #8d348793;
    }

    .thead6{
        background-color: #ffbb4e;
    }

    .thead7{
        background-color: #ffff44;
    }

    .thead4-eqp{
        align-items: center;
        background-color: #b1ffa7;
        border-bottom: 1px solid #1eff00;
    }

    .thead1 th,
    .thead2 th,
    .thead3 th,
    .thead4 th,
    .thead5 th,
    .thead6 th,
    .thead7 th{
        padding: 10px;
        text-align: center;
    }

    .thead4-eqp{
        text-align: center;
    }

    .thead1 img,
    .thead2 img,
    .thead3 img,
    .thead4 img,
    .thead5 img,
    .thead6 img,
    .thead7 img,
    .thead4-eqp img{
        vertical-align: middle;
        margin-left: 10px;
        width: 20px;
        height: auto;
    }

    .tdata1 td,
    .tdata2 td,
    .tdata3 td,
    .tdata4 td,
    .tdata5 td,
    .tdata6 td,
    .tdata7 td{
        padding: 10px;
    }

    .tdata1 td{
        border-top: 1px solid #008cff;
        background-color: #c8e6ff;
    }

    .tdata2 td{
        border-top: 1px solid #ffb7c9;
        background-color: #ffd8fd;
    }

    .tdata3 td{
        border-top: 1px solid #ff2600;
        background-color: #ffe1d7;
    }

    .tdata4 td{
        /* border-top: 1px solid #1eff00; */
        background-color: #ccffc5;
    }

    .tdata5 td{
        border-top: 1px solid #96008c93;
        background-color: #e2cee193;
    }

    .tdata6 td{
        border-top: 1px solid #f3aa47;
        background-color: #fff7d5;
    }

    .tdata7 td{
        border-top: 1px solid #b3b301;
        background-color: #ffffc3;
    }

    .flex-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .flex-row {
        display: flex;
        justify-content: center;
        margin-bottom: 5px;
        height: auto;
    }

    .flex-column {
        display: flex;
        flex-direction: column;
        height: auto;
        max-height: 100px;
        min-width: 400px;
    }"""

html = tableGeral()

st.write(f'<div>{html}</div>', unsafe_allow_html=True)
st.write(f'<style>{canvaStyle}</style>', unsafe_allow_html=True)