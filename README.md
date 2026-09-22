# SecureBioIoT — Arquitetura Segura para Transmissão de Sinais Biomédicos em Dispositivos IoT

Subprojeto de Iniciação Científica (IC) vinculado ao projeto guarda-chuva **"Inteligência Artificial Confiável e Segura Aplicada à Saúde Digital"** da **Universidade Federal de Itajubá (UNIFEI)**.

---

## 📌 Descrição do Projeto

O **SecureBioIoT** visa projetar, implementar e avaliar uma arquitetura de baixo custo baseada em dispositivos IoT (**ESP32**) para a transmissão de sinais eletrocardiográficos (ECG) com garantias de segurança. 


---

## 🔄 Fluxo de Dados e Arquitetura do Sistema

A transmissão de dados ocorre no seguinte fluxo modular:

```text
[ Dados ECG Públicos ]
          │
          ▼
[ ESP32 (Processamento & Cifragem) ]
          │
          ▼
[ Rede (Wi-Fi / TLS) ]
          │
          ▼
[ Servidor Backend (Validação & Logs) ]
          │
          ▼
[ Análise de Métricas (CPU, Latência, Memória) ]
```
## 🛠️ Tecnologias e Ferramentas

* **Microcontrolador:** ESP32
* **Linguagens de Programação:** C/C++ (firmware ESP32) e Python (backend/scripts de simulação)
* **Protocolos & Comunicação:** TCP/IP, MQTT, HTTP, TLS/SSL
* **Versionamento & Gestão:** Git, GitHub, VS Code