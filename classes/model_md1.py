import math
class ModelMD1:
    
    def __init__(self, lam, mu):
        """
        Конструктор класса
        λ - Частота поступления запросов
        μ - Частота обслуживания сервером
        """
        self.lam = lam 
        self.mu  = mu 
    
    def is_valid(self):
        # μ должна быть больше λ
        return self.mu > self.lam

    def md1(self):
        result = {
            'lam': self.lam,
            'mu':  self.mu,
            'models': 'md1'
        }
        if not self.is_valid():
            result['log'] = '<span class="red">Значение <b>µ</b> должно быть больше <b>λ</b></span>'
            return result
        try:
            # Коэффициент использования серверов: U = λ / (λ + µ)
            U = self.lam / (self.lam + self.mu)
            
            # Вероятность того, что система не занята
            P0 = (self.lam / self.mu) / (1 + (self.lam / self.mu)) # P0 = (λ / µ)/(1 + (λ / µ))
            
            # Среднее количество запросов в системе
            L = 2 * (self.lam / (self.lam + self.mu)) / (1 - (self.lam / (self.lam + self.mu))) # L = 2 × U/(1 – U)
            
            # Среднее время в системе
            W = 1 /  (self.mu - self.lam) # W = 1/(µ – λ) 
            
            result.update({
                'U':    f"{U:.3f}",
                'P0':   f"{P0:.3f}",
                'L':    f"{L:.3f}",
                'W':    f"{W:.3f}",
                'state': 'true',
                'log': '<span class="green">Данные успешно рассчитаны (md1)</span>'
            })
            return result
            
        except OverflowError:
            result['log'] = '<span class="red">Ошибка: слишком большое значение "c (количество серверов)"</span>'
            return result
