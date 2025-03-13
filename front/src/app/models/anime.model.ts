export interface Anime {
  id: number;
  title: string;
  author: string;
  genre: string;
  amountEpisodes: number;
  image: string;
}

// Opcionalmente, puedes definir una interface para la respuesta de la API
export interface JikanResponse {
  data: JikanAnime[];
  pagination: {
    last_visible_page: number;
    has_next_page: boolean;
    current_page: number;
  };
}

export interface JikanAnime {
  mal_id: number;
  title: string;
  title_english: string;
  images: {
    jpg: {
      image_url: string;
    };
  };
  episodes: number;
  aired: {
    from: string;
  };
  studios: {
    name: string;
  }[];
  genres: {
    name: string;
  }[];
  // Otros campos que vienen en la respuesta
}
