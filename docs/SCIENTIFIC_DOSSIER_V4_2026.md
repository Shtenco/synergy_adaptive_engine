# ADAPTIVE ENGINE / ONLINE EXPERTS

## Ведущая идея и реализованное математическое ядро

AdaptiveEnsemble performs soft exponential multiplicative updates of strategy weights from clipped rewards, with eta=0.25 and proposed max_step=0.15. It emits a simplex weighted signal score. A separate regime rule classifies sample return-volatility.

## Количественное описание

TargetWeight_i = Weight_i*exp(eta*clip(reward_i,-1,1))/sum_j(Weight_j*exp(eta*clip(reward_j,-1,1))). Each difference from present weights is clipped before weights are made nonnegative and renormalized. Final actual step may exceed max_step due to renormalization.

## Новая экспериментальная программа

Compare exponential experts, uniform and regime-conditioned approaches on frozen OOS sequential tasks. Study clipping, post-renormalization step guarantee, null rewards, extreme losses, turnover and post-fee performance.

## Интеграция в институциональную архитектуру

Исходные сигналы остаются исследовательскими рекомендациями. Перед допуском в execution необходимы независимая валидация QuantLab, свежий риск-стейт RiskGuard и явные права оператора. Положительный исследовательский score, котировка или вес стратегии не означают исполненную или прибыльную торговую операцию.

## Источники и правила публикации

- [src/synergy_adaptive_engine/core.py](../src/synergy_adaptive_engine/core.py)
- [src/synergy_adaptive_engine/synergy_contracts.py](../src/synergy_adaptive_engine/synergy_contracts.py)
- [tests/](../tests/)

Следующая версия должна фиксировать source SHA, dataset hash, временные окна, конфигурацию и воспроизведённые результаты. Прежняя документация сохраняется целиком.
