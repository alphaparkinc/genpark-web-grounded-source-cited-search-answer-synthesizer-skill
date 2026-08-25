from client import WebGroundedSourceCitedSearchAnswerSynthesizerClient

def main():
    client = WebGroundedSourceCitedSearchAnswerSynthesizerClient()
    res = client.synthesize_grounded_web_answer('Global semiconductor EUV lithography market share 2026')
    print('Search Session: ' + res['search_session_id'] + ' (' + str(res['live_web_domains_crawled_count']) + ' domains crawled)')
    print('Faithfulness: ' + str(res['groundedness_faithfulness_score_pct']) + '% | Recency: ' + res['recency_window'])
    for c in res['inline_academic_source_citations']:
        print('  [' + str(c['citation_index']) + '] ' + c['domain'] + ' - ' + c['title'])

if __name__ == '__main__':
    main()
