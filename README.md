# SecureBioIoT — Arquitetura Segura para Transmissão de Sinais Biomédicos em Dispositivos IoT

Subprojeto de Iniciação Científica (IC) vinculado ao projeto guarda-chuva **"Inteligência Artificial Confiável e Segura Aplicada à Saúde Digital"** da **Universidade Federal de Itajubá (UNIFEI)**.

---

## 📌 Descrição do Projeto

O **SecureBioIoT** visa projetar, implementar e avaliar uma arquitetura de baixo custo baseada em dispositivos IoT (**ESP32**) para a transmissão de sinais eletrocardiográficos (ECG) com garantias de segurança. 


---

## 🔄 Fluxo de Dados e Arquitetura do Sistema

A transmissão de dados ocorre no seguinte fluxo modular:

+-------------------------------------------------------+
|                 1. FONTE DE DADOS                     |
|  Bases Públicas / Dados Sintéticos de ECG (Anonimizados)|
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|                 2. DISPOSITIVO IoT                    |
|                    (ESP32)                            |
|  - Processamento do sinal biomédico                   |
|  - Aplicação dos Controles de Segurança               |
|    (Cifragem, Autenticação, Integridade)              |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|               3. CANAL DE COMUNICAÇÃO                 |
|             (Wi-Fi / MQTT / TCP com TLS)              |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|                 4. SERVIDOR / BACKEND                 |
|  - Recepção e Validação dos Pacotes                   |
|  - Descifragem e Verificação de Integridade           |
|  - Armazenamento Seguro e Registos de Auditoria (Logs)|
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|              5. MÉTRICAS E AVALIAÇÃO                  |
|  - Análise de Desempenho (Latência, CPU, Memória)     |
|  - Validação para o TCC / Artigo Científico           |
+-------------------------------------------------------+
## 🛠️ Tecnologias e Ferramentas

* **Microcontrolador:** ESP32
* **Linguagens de Programação:** C/C++ (firmware ESP32) e Python (backend/scripts de simulação)
* **Protocolos & Comunicação:** TCP/IP, MQTT, HTTP, TLS/SSL
* **Versionamento & Gestão:** Git, GitHub, VS Code