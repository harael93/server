# Tarot API Server

A Django REST API for tarot card management and readings.

## Deployment from Git

1. **Clone the repository**
   ```bash
   git clone https://github.com/harael93/server.git
   cd server
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start server**
   ```bash
   python manage.py runserver
   ```

Server will be available at: `http://localhost:8000`

---

## Card Operations

### List All Cards
**GET** `/api/cards/`

View all tarot cards in the database.

```bash
curl "http://localhost:8000/api/cards/"
```

```javascript
fetch('http://localhost:8000/api/cards/')
  .then(response => response.json())
  .then(cards => console.log(cards));
```

### Search Card by Name
**GET** `/api/search/?q={name}`

Find a specific card by searching its name.

```bash
# Search for "The Fool"
curl "http://localhost:8000/api/search/?q=fool"

# Search for "Ace of Cups"  
curl "http://localhost:8000/api/search/?q=ace%20of%20cups"
```

```javascript
// Search for a card
const searchCard = async (cardName) => {
  const response = await fetch(`http://localhost:8000/api/search/?q=${encodeURIComponent(cardName)}`);
  const data = await response.json();
  return data.results;
};

// Usage
searchCard("The Fool").then(cards => console.log(cards));
```

### Draw Three Cards
**GET** `/api/draw-three/`

Draw 3 random cards for a Past/Present/Future reading.

```bash
curl "http://localhost:8000/api/draw-three/"
```

```javascript
const drawThreeCards = async () => {
  const response = await fetch('http://localhost:8000/api/draw-three/');
  const reading = await response.json();
  return reading;
};

// Usage
drawThreeCards().then(reading => {
  console.log(reading.reading_type); // "3-Card Past/Present/Future Reading"
  reading.reading.forEach(card => {
    console.log(`${card.position}: ${card.card.title} (${card.orientation})`);
    console.log(`Meaning: ${card.meaning}`);
  });
});
```

### Draw Ten Cards  
**GET** `/api/draw-ten/`

Draw 10 random cards for a Celtic Cross reading.

```bash
curl "http://localhost:8000/api/draw-ten/"
```

```javascript
const drawTenCards = async () => {
  const response = await fetch('http://localhost:8000/api/draw-ten/');
  const reading = await response.json();
  return reading;
};

// Usage
drawTenCards().then(reading => {
  console.log(reading.reading_type); // "10-Card Celtic Cross Reading"
  reading.reading.forEach(card => {
    console.log(`${card.position}: ${card.card.title} (${card.orientation})`);
  });
});
```

---

## Response Format

All card responses include:
- `id`: Card ID
- `title`: Card name (e.g., "The Fool", "Ace of Cups")
- `suite`: "major", "cups", "wands", "swords", or "pentacles"  
- `image`: Full URL to card image
- `upright_meaning`: Meaning when upright
- `reversed_meaning`: Meaning when reversed
- `element`, `astrological_sign`, `planet`: Optional correspondences

Reading responses include card orientation (`upright` or `reversed`) and the appropriate meaning.

---

## Web Interface

- **Card Management**: `http://localhost:8000/api/manage/`
- **Admin Panel**: `http://localhost:8000/admin/`
