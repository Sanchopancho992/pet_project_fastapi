export function setPlayerNameLocalStorage(game_id: string, playerName: string){
  localStorage.setItem(`game_id:${game_id}`, playerName);

}

export function getPlayerNameFromLocalStorage(game_id:string) {
  if (typeof window !== 'undefined') {
    return localStorage.getItem(`game_id:${game_id}`);
  }
}