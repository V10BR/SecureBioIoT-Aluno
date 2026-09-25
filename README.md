# SecureBioIoT

## Arquitetura segura para transmissão de sinais biomédicos em dispositivos IoT

O **SecureBioIoT** é um projeto voltado ao estudo de segurança em sistemas IoT aplicados à transmissão de sinais biomédicos.

O projeto busca desenvolver uma arquitetura capaz de transmitir dados biomédicos de forma segura, considerando aspectos como **confidencialidade, integridade, autenticação e confiabilidade**.

## Objetivos

* Estudar a aplicação de segurança em dispositivos IoT.
* Desenvolver um protótipo utilizando ESP32.
* Trabalhar com sinais de ECG públicos ou sintéticos.
* Implementar comunicação entre dispositivo e servidor.
* Aplicar mecanismos de segurança à transmissão dos dados.
* Avaliar o funcionamento e a segurança da arquitetura desenvolvida.

## Arquitetura

O sistema utiliza um fluxo de comunicação entre um dispositivo IoT e um servidor:

```text
Sinal ECG
   |
   v
ESP32
   |
   v
Rede(MQTT)
   |
   v
Servidor
```

A arquitetura poderá ser expandida conforme o desenvolvimento do projeto.

## Tecnologias

* ESP32
* MQTT
* Wi-Fi
* TCP/IP
* Python
* C/C++
* Git

## Segurança

Entre os conceitos abordados pelo projeto estão:

* Autenticação
* Autorização
* Criptografia
* Integridade de dados
* Proteção contra replay
* Gestão de credenciais
* Auditoria e registros de eventos

## Estrutura

```text
SecureBioIoT/
├── backend/
├── firmware/
├── docs/
├── experiments/
├── scripts/
├── tests/
└── README.md
```

A estrutura do projeto poderá ser alterada conforme sua evolução.

## Status

Em desenvolvimento.

## Projeto

**SecureBioIoT**
Cibersegurança, IoT e Saúde Digital
